#!./runmodule.sh

'''
This module defines the ConfigFile class
which can be used to load and save config files.
'''

import os
import shlex
import enum
import functools
import argparse
import inspect
import abc
import typing
from collections.abc import Iterable, Iterator, Sequence, Callable

import appdirs

from .config import Config, DictConfig, MultiConfig, ConfigId

if typing.TYPE_CHECKING:
	from typing_extensions import Unpack, Required


#: If the name or an alias of :class:`ConfigFileCommand` is this value that command is used by :meth:`ConfigFile.parse_splitted_line` if an undefined command is encountered.
DEFAULT_COMMAND = ''


def readable_quote(value: str) -> str:
	'''
	This function has the same goal like :func:`shlex.quote` but tries to generate better readable output.

	:param value: A value which is intended to be used as a command line argument
	:return: A POSIX compliant quoted version of :paramref:`value`
	'''
	out = shlex.quote(value)
	if out == value:
		return out

	if '"\'"' in out and '"' not in value:
		return '"' + value + '"'

	return out


@functools.total_ordering
class SortedEnum(enum.Enum):

	def __lt__(self, other: typing.Any) -> bool:
		if self.__class__ is other.__class__:
			l: 'Sequence[SortedEnum]' = list(type(self))
			return l.index(self) < l.index(other)
		return NotImplemented

@enum.unique
class NotificationLevel(SortedEnum):
	INFO = 'info'
	ERROR = 'error'

UiCallback: 'typing.TypeAlias' = 'Callable[[NotificationLevel, str|BaseException], None]'

class UiNotifier:

	'''
	Most likely you will want to load the config file before creating the UI.
	But if there are errors in the config file the user will want to know about them.
	This class takes the messages from :class:`ConfigFile` and stores them until the UI is ready.
	When you call :meth:`set_ui_callback` the stored messages will be forwarded and cleared.

	This object can also filter the messages.
	:class:`ConfigFile` calls :meth:`show_info` every time a setting is changed.
	If you load an entire config file this can be many messages and the user probably does not want to see them all.
	Therefore this object drops all messages of :const:`NotificationLevel.INFO` by default.
	Pass :obj:`notification_level` to the constructor if you don't want that.
	'''

	# ------- public methods -------

	def __init__(self, notification_level: 'Config[NotificationLevel]|NotificationLevel' = NotificationLevel.ERROR) -> None:
		self._messages: 'list[tuple[NotificationLevel, str|BaseException]]' = []
		self._callback: 'UiCallback|None' = None
		self._notification_level = notification_level

	def set_ui_callback(self, callback: UiCallback) -> None:
		self._callback = callback

		for lvl, msg in self._messages:
			callback(lvl, msg)
		self._messages.clear()


	@property
	def notification_level(self) -> NotificationLevel:
		if isinstance(self._notification_level, Config):
			return self._notification_level.value
		else:
			return self._notification_level

	@notification_level.setter
	def notification_level(self, val: NotificationLevel) -> None:
		if isinstance(self._notification_level, Config):
			self._notification_level.value = val
		else:
			self._notification_level = val


	# ------- called by ConfigFile -------

	def show_info(self, msg: str, *, ignore_filter: bool = False) -> None:
		self.show(NotificationLevel.INFO, msg, ignore_filter=ignore_filter)

	def show_error(self, msg: 'str|BaseException', *, ignore_filter: bool = False) -> None:
		self.show(NotificationLevel.ERROR, msg, ignore_filter=ignore_filter)


	# ------- internal methods -------

	def show(self, notification_level: NotificationLevel, msg: 'str|BaseException', *, ignore_filter: bool = False) -> None:
		if notification_level < self.notification_level and not ignore_filter:
			return

		if self._callback:
			self._callback(notification_level, msg)
		else:
			self._messages.append((notification_level, msg))


class ParseException(Exception):

	'''
	This is raised and caught inside of :class:`ConfigFile` to communicate errors while parsing a config file.
	If you don't intend to subclass :class:`ConfigFile` you do not need to worry about this class.
	'''

class MultipleParseExceptions(Exception):

	'''
	This is raised and caught inside of :class:`ConfigFile` to communicate errors while parsing a config file where multiple settings are set in the same line.
	If you don't intend to subclass :class:`ConfigFile` you do not need to worry about this class.
	'''

	def __init__(self, exceptions: 'Sequence[ParseException]') -> None:
		super().__init__()
		self.exceptions = exceptions

	def __iter__(self) -> 'Iterator[ParseException]':
		return iter(self.exceptions)


if hasattr(typing, 'TypedDict'):  # python >= 3.8
	class SaveKwargs(typing.TypedDict, total=False):
		config_instances: 'Iterable[Config[typing.Any] | DictConfig[typing.Any, typing.Any]]'
		ignore: 'Iterable[Config[typing.Any] | DictConfig[typing.Any, typing.Any]] | None'
		no_multi: bool
		comments: bool

	class ParseLineKwargs(typing.TypedDict, total=False):
		file_name: str
		line_number: int

	class ParseSplittedLineKwargs(ParseLineKwargs, total=False):
		line: 'Required[str]'


class ConfigFile:

	'''
	Read or write a config file.
	'''

	#: The name of the config file used by :meth:`iter_config_paths`. Can be changed with the environment variable ``CONFATTR_FILENAME``.
	FILENAME = os.environ.get('CONFATTR_FILENAME', 'config')

	COMMENT = '#'
	COMMENT_PREFIXES = ('"', '#')
	ENTER_GROUP_PREFIX = '['
	ENTER_GROUP_SUFFIX = ']'


	def __init__(self, *,
		notification_level: 'Config[NotificationLevel]|NotificationLevel' = NotificationLevel.ERROR,
		appname: str,
		authorname: 'str|None' = None,
		config_instances: 'dict[str, Config[typing.Any]]' = Config.instances,
		commands: 'Sequence[type[ConfigFileCommand]]|None' = None,
	) -> None:
		'''
		:param notification_level: Messages of a lower priority are *not* passed to the callback registered with :meth:`set_ui_callback`
		:param appname: The name of the application, required for generating the path of the config file if you use :meth:`load` or :meth:`save`
		:param authorname: The name of the developer of the application, on MS Windows useful for generating the path of the config file if you use :meth:`load` or :meth:`save`
		:param config_instances: The Config instances to load or save, defaults to :attr:`Config.instances`
		:param commands: The :class:`ConfigFileCommand`s allowed in this config file, if this is :const:`None`: use the return value of :meth:`ConfigFileCommand.get_command_types`
		'''
		self.appname = appname
		self.authorname = authorname
		self.ui_notifier = UiNotifier(notification_level)
		self.config_instances = config_instances
		self.config_id: 'ConfigId|None' = None

		if commands is None:
			commands = ConfigFileCommand.get_command_types()
		self.commands = {}
		for cmd in commands:
			for name in cmd.get_names():
				self.commands[name] = cmd(self)


	def set_ui_callback(self, callback: UiCallback) -> None:
		'''
		Register a callback to a user interface in order to show messages to the user like syntax errors or invalid values in the config file.

		Messages which occur before this method is called are stored and forwarded as soon as the callback is registered.

		:param ui_callback: A function to display messages to the user
		'''
		self.ui_notifier.set_ui_callback(callback)

	def get_app_dirs(self) -> 'appdirs.AppDirs':
		'''
		Create or get a cached `AppDirs <https://github.com/ActiveState/appdirs/blob/master/README.rst#appdirs-for-convenience>`_ instance with multipath support enabled.

		When creating a new instance, `platformdirs <https://pypi.org/project/platformdirs/>`_, `xdgappdirs <https://pypi.org/project/xdgappdirs/>`_ and `appdirs <https://pypi.org/project/appdirs/>`_ are tried, in that order.
		The first one installed is used.
		appdirs, the original of the two forks and the only one of the three with type stubs, is specified in pyproject.toml as a hard dependency so that at least one of the three should always be available.
		I am not very familiar with the differences but if a user finds that appdirs does not work for them they can choose to use an alternative with ``pipx inject appname xdgappdirs|platformdirs``.

		These libraries should respect the environment variables ``XDG_CONFIG_HOME`` and ``XDG_CONFIG_DIRS``.
		'''
		if not hasattr(self, '_appdirs'):
			try:
				import platformdirs  # type: ignore [import]  # this library is not typed and not necessarily installed, I am relying on it's compatibility with appdirs
				AppDirs = typing.cast('type[appdirs.AppDirs]', platformdirs.PlatformDirs)
			except ImportError:
				try:
					import xdgappdirs  # type: ignore [import]  # this library is not typed and not necessarily installed, I am relying on it's compatibility with appdirs
					AppDirs = typing.cast('type[appdirs.AppDirs]', xdgappdirs.AppDirs)
				except ImportError:
					AppDirs = appdirs.AppDirs

			self._appdirs = AppDirs(self.appname, self.authorname, multipath=True)

		return self._appdirs

	# ------- load -------

	def iter_user_site_config_paths(self) -> 'Iterator[str]':
		'''
		Iterate over all directories which are searched for config files, user specific first.

		The directories are based on :meth:`get_app_dirs`.
		'''
		appdirs = self.get_app_dirs()
		yield from appdirs.user_config_dir.split(os.path.pathsep)
		yield from appdirs.site_config_dir.split(os.path.pathsep)

	def iter_config_paths(self) -> 'Iterator[str]':
		'''
		Iterate over all paths which are checked for config files, user specific first.

		Use this method if you want to tell the user where the application is looking for it's config file.
		The first existing file yielded by this method is used by :meth:`load`.

		The paths are generated by joining the directories yielded by :meth:`iter_user_site_config_paths` with
		:attr:`ConfigFile.FILENAME` (the value of the environment variable ``CONFATTR_FILENAME`` if it is set or ``'config'``).
		'''
		for path in self.iter_user_site_config_paths():
			yield os.path.join(path, self.FILENAME)

	def load(self) -> None:
		'''
		Load the first existing config file returned by :meth:`iter_config_paths`.

		If there are several config files a user specific config file is preferred.
		If a user wants a system wide config file to be loaded, too, they can explicitly include it in their config file.
		'''
		for fn in self.iter_config_paths():
			if os.path.isfile(fn):
				self.load_file(fn)
				return

	def load_file(self, fn: str) -> None:
		'''
		Load a config file and change the :class:`Config` objects accordingly.

		Use :meth:`set_ui_callback` to get error messages which appeared while loading the config file.
		You can call :meth:`set_ui_callback` after this method without loosing any messages.

		:param fn: The file name of the config file (absolute or relative path)
		'''
		self.config_id = None
		self.load_without_resetting_config_id(fn)

	def load_without_resetting_config_id(self, fn: str) -> None:
		with open(fn, 'rt') as f:
			for lnno, ln in enumerate(f, 1):
				self.parse_line(line=ln, line_number=lnno, file_name=f.name)

	def parse_line(self, line: str, **kw: 'Unpack[ParseLineKwargs]') -> None:
		'''
		:param line: The line to be parsed
		:param line_number: The number of the line, used in error messages
		:param file_name: The name of the file from which ln was read (absolute or relative path), used in error messages and for relative imports

		:paramref:`line_number` and :paramref:`file_name` don't need to be passed in case :paramref:`ln` is not read from a config file but from a command line.

		:meth:`parse_error` is called if something goes wrong, e.g. invalid key or invalid value.
		'''
		ln = line.strip()
		if not ln:
			return
		if self.is_comment(ln):
			return
		if self.enter_group(ln):
			return

		ln_splitted = shlex.split(ln, comments=True)
		kw2 = typing.cast('ParseSplittedLineKwargs', kw)
		kw2['line'] = ln
		self.parse_splitted_line(ln_splitted, **kw2)

	def is_comment(self, ln: str) -> bool:
		'''
		Check if :paramref:`ln` is a comment.

		:param ln: The current line
		:return: :const:`True` if :paramref:`ln` is a comment
		'''
		for c in self.COMMENT_PREFIXES:
			if ln.startswith(c):
				return True
		return False

	def enter_group(self, ln: str) -> bool:
		'''
		Check if :paramref:`ln` starts a new group and set :attr:`config_id` if it does.

		:param ln: The current line
		:return: :const:`True` if :paramref:`ln` starts a new group
		'''
		if ln.startswith(self.ENTER_GROUP_PREFIX) and ln.endswith(self.ENTER_GROUP_SUFFIX):
			self.config_id = typing.cast(ConfigId, ln[len(self.ENTER_GROUP_PREFIX):-len(self.ENTER_GROUP_SUFFIX)])
			if self.config_id not in MultiConfig.config_ids:
				MultiConfig.config_ids.append(self.config_id)
			return True
		return False

	def parse_splitted_line(self, ln_splitted: 'Sequence[str]', **kw: 'Unpack[ParseSplittedLineKwargs]') -> None:
		cmd_name = ln_splitted[0]

		try:
			if cmd_name in self.commands:
				cmd = self.commands[cmd_name]
			elif DEFAULT_COMMAND in self.commands:
				cmd = self.commands[DEFAULT_COMMAND]
			else:
				cmd = UnknownCommand(self)
			cmd.run(ln_splitted, **kw)
		except ParseException as e:
			self.parse_error(str(e), **kw)
		except MultipleParseExceptions as exceptions:
			for exc in exceptions:
				self.parse_error(str(exc), **kw)


	# ------- save -------

	def save(self,
		**kw: 'Unpack[SaveKwargs]',
	) -> str:
		'''
		Save the current values of all settings to the first existing and writable file returned by :meth:`iter_config_paths` or to the first path if none of the files are existing and writable.

		In case no writable file is found the directories are created as necessary.

		:param config_instances: Do not save all settings but only those given. If this is a :class:`list` they are written in the given order. If this is a :class:`set` they are sorted by their keys.
		:param ignore: Do not write these settings to the file.
		:param no_multi: Do not write several sections. For :class:`MultiConfig` instances write the default values only.
		:param comments: Write comments with allowed values and help.
		:return: The path to the file which has been written
		'''
		paths = tuple(self.iter_config_paths())
		for fn in paths:
			if os.path.isfile(fn) and os.access(fn, os.W_OK):
				break
		else:
			fn = paths[0]
			os.makedirs(os.path.dirname(fn), exist_ok=True)
		self.save_file(fn, **kw)
		return fn

	def save_file(self,
		fn: str,
		**kw: 'Unpack[SaveKwargs]'
	) -> None:
		'''
		Save the current values of all settings to a specific file.

		:param fn: The name of the file to write to. If this is not an absolute path it is relative to the current working directory.
		:raises FileNotFoundError: if the directory does not exist

		For an explanation of the other parameters see :meth:`save`.
		'''
		with open(fn, 'wt') as f:
			self.save_to_open_file(f, **kw)


	def save_to_open_file(self,
		f: typing.TextIO,
		**kw: 'Unpack[SaveKwargs]',
	) -> None:
		'''
		Save the current values of all settings to file-like object.

		:param f: The file to write to

		For an explanation of the other parameters see :meth:`save`.
		'''
		kw.setdefault('config_instances', set(self.config_instances.values()))
		kw.setdefault('ignore', None)
		kw.setdefault('no_multi', False)
		kw.setdefault('comments', True)

		for cmd in self.commands.values():
			cmd.save(f, **kw)


	def quote(self, val: str) -> str:
		'''
		Quote a value if necessary so that it will be interpreted as one argument.

		The default implementation calls :func:`readable_quote`.
		'''
		return readable_quote(val)

	def write_config_id(self, f: typing.TextIO, config_id: ConfigId) -> None:
		'''
		Start a new group in the config file so that all following commands refer to the given :paramref:`config_id`.
		'''
		f.write(self.ENTER_GROUP_PREFIX + config_id + self.ENTER_GROUP_SUFFIX + '\n')


	# ------- error handling -------

	def parse_error(self, msg: str, **kw: 'Unpack[ParseSplittedLineKwargs]') -> None:
		'''
		Is called if something went wrong while trying to load a config file.

		This method is called when a :class:`ParseException` or :class:`MultipleParseExceptions` is caught.
		This method compiles the given information into an error message and calls :meth:`UiNotifier.show_error`.

		:param msg: The error message
		:param line: The line where the error occured
		:param line_number: The number of the line
		:param file_name: The name of the config file from which the line has been read
		'''
		ln = kw['line']
		lnno = kw.get('line_number', None)
		if lnno is not None:
			lnref = 'line %s' % lnno
		else:
			lnref = 'line'
		msg +=  f' while trying to parse {lnref} {ln!r}'
		self.ui_notifier.show_error(msg)


class ConfigFileCommand(abc.ABC):

	'''
	An abstract base class for commands which can be used in a config file.

	Subclasses must implement the :meth:`run` method which is called when :class:`ConfigFile` is loading a file.
	Subclasses should contain a doc string so that :meth:`get_help` can provide a description to the user.
	Subclasses may set the :attr:`name` and :attr:`aliases` attributes to change the output of :meth:`get_name` and :meth:`get_names`.

	All subclasses are remembered and can be retrieved with :meth:`get_command_types`.
	They are instantiated in the constructor of :class:`ConfigFile`.
	'''

	#: The name which is used in the config file to call this command. Use an empty string to define a default command which is used if an undefined command is encountered. If this is not set :meth:`get_name` returns the name of this class in lower case letters and underscores replaced by hyphens.
	name: str

	#: Alternative names which can be used in the config file.
	aliases: 'tuple[str, ...]|list[str]'

	#: A description which may be used by an in-app help. If this is not set :meth:`get_help` uses the doc string instead.
	help: str

	_subclasses: 'list[type[ConfigFileCommand]]' = []
	_used_names: 'set[str]' = set()

	@classmethod
	def get_command_types(cls) -> 'tuple[type[ConfigFileCommand], ...]':
		'''
		:return: All subclasses of :class:`ConfigFileCommand` which have not been deleted with :meth:`delete_command_type`
		'''
		return tuple(cls._subclasses)

	@classmethod
	def delete_command_type(cls, cmd: 'type[ConfigFileCommand]') -> None:
		'''
		Delete :paramref:`cmd` so that it is not returned anymore by :meth:`get_command_types` and that it's name can be used by another command.
		Do nothing if :paramref:`cmd` has already been deleted.
		'''
		if cmd in cls._subclasses:
			cls._subclasses.remove(cmd)
			for name in cmd.get_names():
				cls._used_names.remove(name)

	@classmethod
	def __init_subclass__(cls, replace: bool = False, abstract: bool = False) -> None:
		'''
		Add the new subclass to :attr:`subclass`.

		:param replace: Set :attr:`name` and :attr:`aliases` to the values of the parent class if they are not set explicitly, delete the parent class with :meth:`delete_command_type` and replace any commands with the same name
		:param abstract: This class is a base class for the implementation of other commands and shall *not* be returned by :meth:`get_command_types`
		:raises ValueError: if the name or one of it's aliases is already in use and :paramref:`replace` is not true
		'''
		if replace:
			parent_commands = [parent for parent in cls.__bases__ if issubclass(parent, ConfigFileCommand)]

			# set names of this class to that of the parent class(es)
			parent = parent_commands[0]
			if 'name' not in cls.__dict__:
				cls.name = parent.get_name()
			if 'aliases' not in cls.__dict__:
				cls.aliases = list(parent.get_names())[1:]
				for parent in parent_commands[1:]:
					cls.aliases.extend(parent.get_names())

			# remove parent class from the list of commands to be loaded or saved
			for parent in parent_commands:
				if issubclass(parent, ConfigFileCommand):
					cls.delete_command_type(parent)

		if not abstract:
			cls._subclasses.append(cls)
			for name in cls.get_names():
				if name in cls._used_names and not replace:
					raise ValueError('duplicate command name %r' % name)
				cls._used_names.add(name)

	@classmethod
	def get_name(cls) -> str:
		'''
		:return: The name which is used in config file to call this command.
		
		If :attr:`name` is set it is returned as it is.
		Otherwise a name is generated based on the class name.
		'''
		if 'name' in cls.__dict__:
			return cls.name
		return cls.__name__.lower().replace("_", "-")

	@classmethod
	def get_names(cls) -> 'Iterator[str]':
		'''
		:return: Several alternative names which can be used in a config file to call this command.
		
		The first one is always the return value of :meth:`get_name`.
		If :attr:`aliases` is set it's items are yielded afterwards.

		If one of the returned items is the empty string this class is the default command
		and :meth:`run` will be called if an undefined command is encountered.
		'''
		yield cls.get_name()
		if 'aliases' in cls.__dict__:
			for name in cls.aliases:
				yield name

	def __init__(self, config_file: ConfigFile) -> None:
		self.config_file = config_file
		self.ui_notifier = config_file.ui_notifier

	@abc.abstractmethod
	def run(self, ln: 'Sequence[str]', **kw: 'Unpack[ParseSplittedLineKwargs]') -> None:
		'''
		Process one line which has been read from a config file

		:raises ParseException: if there is an error in the line (e.g. invalid syntax)
		:raises MultipleParseExceptions: if there are several errors in the same line
		'''
		raise NotImplementedError()

	@classmethod
	def get_help(cls) -> str:
		'''
		:return: A help text which can be presented to the user.
		         The default implementation returns :attr:`help` if given or the doc string otherwise, preprocessed by :func:`inspect.cleandoc`.
		'''
		if hasattr(cls, 'help'):
			doc = cls.help
		elif cls.__doc__:
			doc = cls.__doc__
		else:
			return ''

		return inspect.cleandoc(doc)


	def save(self,
		f: typing.TextIO,
		**kw: 'Unpack[SaveKwargs]',
	) -> None:
		'''
		Write as many calls to this command as necessary to the config file in order to create the current state.
		There is the :attr:`config_file` attribute (which was passed to the constructor) which you can use to:
		- quote arguments with :meth:`ConfigFile.quote`
		- get the comment character :attr:`ConfigFile.COMMENT`
		- call :attr:`write_config_id`

		The default implementation does nothing.
		'''
		pass


class ArgumentParser(argparse.ArgumentParser):

	def error(self, message: str) -> 'typing.NoReturn':
		raise ParseException(message)

class ConfigFileArgparseCommand(ConfigFileCommand, abstract=True):

	'''
	An abstract subclass of :class:`ConfigFileCommand` which uses :mod:`argparse` to make parsing and providing help easier.

	You must implement the class method :meth:`init_parser` to add the arguments to :attr:`parser`.
	Instead of :meth:`run` you must implement :meth:`run_parsed`.
	You don't need to add a usage or the possible arguments to the doc string as :mod:`argparse` will do that for you.
	You should, however, still give a description what this command does in the doc string.

	You may specify :attr:`ConfigFileCommand.name`, :attr:`ConfigFileCommand.aliases` and :meth:`ConfigFileCommand.save` like for :class:`ConfigFileCommand`.
	'''

	parser: ArgumentParser
	_names: 'set[str]'

	@classmethod
	def __init_subclass__(cls, replace: bool = False, abstract: bool = False) -> None:
		super().__init_subclass__(replace=replace, abstract=abstract)
		cls.parser = ArgumentParser(prog=cls.get_name(), description=super().get_help(), add_help=False)
		cls.init_parser()
		cls._names = set(cls.get_names())

	@classmethod
	@abc.abstractmethod
	def init_parser(cls) -> None:
		'''
		This is an abstract method which must be implemented by subclasses.
		Use :meth:`ArgumentParser.add_argument` to add arguments to :attr:`parser`.
		'''
		pass

	@classmethod
	def get_help(cls) -> str:
		'''
		:return: A help text which can be presented to the user.
		         This is generated by :meth:`ArgumentParser.format_help`.
		         The return value of :meth:`ConfigFileCommand.get_help` has been passed as :paramref:`description` to the constructor of :class:`ArgumentParser`, therefore :attr:`help`/the doc string are included as well.
		'''
		return cls.parser.format_help().rstrip('\n')

	def run(self, ln: 'Sequence[str]', **kw: 'Unpack[ParseSplittedLineKwargs]') -> None:
		# if the line was empty this method should not be called but an empty line should be ignored either way
		if not ln:
			return
		# ln[0] does not need to be in self._names if this is the default command, i.e. if '' in self._names
		if ln[0] in self._names:
			ln = ln[1:]
		args = self.parser.parse_args(ln)
		self.run_parsed(args)

	@abc.abstractmethod
	def run_parsed(self, args: argparse.Namespace) -> None:
		'''
		This is an abstract method which must be implemented by subclasses.
		'''
		pass


class Set(ConfigFileCommand):

	#: The separator which is used between a key and it's value
	KEY_VAL_SEP = '='

	#: data types which have no help, these are skipped by :meth:`write_data_types`
	primitive_types = {str, int, bool, float}


	# ------- load -------

	def run(self, cmd: 'Sequence[str]', **kw: 'Unpack[ParseSplittedLineKwargs]') -> None:
		'''
		Call :meth:`set_multiple` if the first argument contains :attr:`KEY_VAL_SEP` otherwise :meth:`set_with_spaces`.

		:raises ParseException: if something is wrong (no arguments given, invalid syntax, invalid key, invalid value)
		'''
		if len(cmd) < 2:
			raise ParseException('no settings given')

		if self.KEY_VAL_SEP in cmd[1]:  # cmd[0] is the name of the command, cmd[1] is the first argument
			self.set_multiple(cmd)
		else:
			self.set_with_spaces(cmd)

	def set_with_spaces(self, cmd: 'Sequence[str]') -> None:
		'''
		Process one line of the format ``set key [=] value``

		:raises ParseException: if something is wrong (invalid syntax, invalid key, invalid value)
		'''
		n = len(cmd)
		if n == 3:
			cmdname, key, value = cmd
			self.parse_key_and_set_value(key, value)
		elif n == 4:
			cmdname, key, sep, value = cmd
			if sep != self.KEY_VAL_SEP:
				raise ParseException(f'seperator between key and value should be {self.KEY_VAL_SEP}, not {sep!r}')
			self.parse_key_and_set_value(key, value)
		elif n == 2:
			raise ParseException(f'missing value or missing {self.KEY_VAL_SEP}')
		else:
			assert n >= 5
			raise ParseException(f'too many arguments given or missing {self.KEY_VAL_SEP} in first argument')

	def set_multiple(self, cmd: 'Sequence[str]') -> None:
		'''
		Process one line of the format ``set key=value [key2=value2 ...]``

		:raises MultipleParseExceptions: if something is wrong (invalid syntax, invalid key, invalid value)
		'''
		exceptions = []
		for arg in cmd[1:]:
			if not self.KEY_VAL_SEP in arg:
				raise ParseException(f'missing {self.KEY_VAL_SEP} in {arg!r}')
			key, value = arg.split(self.KEY_VAL_SEP, 1)
			try:
				self.parse_key_and_set_value(key, value)
			except ParseException as e:
				exceptions.append(e)
		if exceptions:
			raise MultipleParseExceptions(exceptions)

	def parse_key_and_set_value(self, key: str, value: str) -> None:
		'''
		Find the corresponding :class:`Config` instance for :paramref:`key` and pass it to :meth:`parse_and_set_value`.

		:raises ParseException: if key is invalid or :meth:`parse_and_set_value` raises a :class:`ValueError`
		'''
		if key not in self.config_file.config_instances:
			raise ParseException(f'invalid key {key!r}')

		instance = self.config_file.config_instances[key]
		try:
			self.parse_and_set_value(instance, value)
		except ValueError as e:
			raise ParseException(str(e))

	def parse_and_set_value(self, instance: Config[typing.Any], value: str) -> None:
		'''
		Parse the given value str and assign it to the given instance by calling :meth:`Config.parse_and_set_value` with :attr:`ConfigFile.config_id` of :attr:`config_file`.
		Afterwards call :meth:`UiNotifier.show_info`.
		'''
		instance.parse_and_set_value(self.config_file.config_id, value)
		self.ui_notifier.show_info(f'set {instance.key} to {instance.format_value(self.config_file.config_id)}')


	# ------- save -------

	def iter_config_instances_to_be_saved(self, **kw: 'Unpack[SaveKwargs]') -> 'Iterator[Config[object]]':
		'''
		:param config_instances: The settings to consider
		:param ignore: Skip these settings

		Iterate over all given :paramref:`config_instances` and expand all :class:`DictConfig` instances into the :class:`Config` instances they consist of.
		Sort the resulting list if :paramref:`config_instances` is not a :class:`list` or a :class:`tuple`.
		Yield all :class:`Config` instances which are not (directly or indirectly) contained in :paramref:`ignore` and where :meth:`Config.wants_to_be_exported` returns true.
		'''
		config_instances = kw['config_instances']
		ignore = kw['ignore']

		config_keys = []
		for c in config_instances:
			if isinstance(c, DictConfig):
				config_keys.extend(sorted(c.iter_keys()))
			else:
				config_keys.append(c.key)
		if not isinstance(config_instances, (list, tuple)):
			config_keys = sorted(config_keys)

		if ignore is not None:
			tmp = set()
			for c in tuple(ignore):
				if isinstance(c, DictConfig):
					tmp |= set(c._values.values())
				else:
					tmp.add(c)
			ignore = tmp

		for key in config_keys:
			instance = self.config_file.config_instances[key]
			if not instance.wants_to_be_exported():
				continue

			if ignore is not None and instance in ignore:
				continue

			yield instance

	def save(self, f: typing.TextIO, **kw: 'Unpack[SaveKwargs]') -> None:
		'''
		:param f: The file to write to
		:param bool no_multi: If true: treat :class:`MultiConfig` instances like normal :class:`Config` instances and only write their default value. If false: Separate :class:`MultiConfig` instances and print them once for every :attr:`MultiConfig.config_ids`.
		:param bool comments: If false: don't call :meth:`write_data_types`.

		Iterate over all :class:`Config` instances with :meth:`iter_config_instances_to_be_saved`,
		split them into normal :class:`Config` and :class:`MultiConfig` and write them with :meth:`save_config_instance`.
		But before that set :attr:`last_name` to None (which is used by :meth:`write_help`) and call :meth:`write_data_types`.
		'''
		no_multi = kw['no_multi']
		comments = kw['comments']

		self.last_name: 'str|None' = None

		config_instances = list(self.iter_config_instances_to_be_saved(**kw))
		if comments:
			self.write_data_types(f, config_instances)

		multi_configs = []
		for instance in config_instances:
			if not no_multi and isinstance(instance, MultiConfig):
				multi_configs.append(instance)
				continue

			self.save_config_instance(f, instance, config_id=None, **kw)

		if multi_configs:
			for config_id in MultiConfig.config_ids:
				f.write('\n')
				self.config_file.write_config_id(f, config_id)
				for instance in multi_configs:
					self.save_config_instance(f, instance, config_id, **kw)

	def save_config_instance(self, f: typing.TextIO, instance: 'Config[object]', config_id: 'ConfigId|None', **kw: 'Unpack[SaveKwargs]') -> None:
		'''
		:param f: The file to write to
		:param instance: The config value to be saved
		:param config_id: Which value to be written in case of a :class:`MultiConfig`, should be :const:`None` for a normal :class:`Config` instance
		:param bool comments: If true: call :meth:`write_help`

		Convert the :class:`Config` instance into a value str with :meth:`format_value`,
		wrap it in quotes if necessary with :meth:`config_file.quote` and print it to :paramref:`f`.
		'''
		if kw['comments']:
			self.write_help(f, instance)
		value = self.format_value(instance, config_id)
		value = self.config_file.quote(value)
		ln = f'{self.get_name()} {instance.key} = {value}\n'
		f.write(ln)

	def format_value(self, instance: Config[typing.Any], config_id: 'ConfigId|None') -> str:
		'''
		:param instance: The config value to be saved
		:param config_id: Which value to be written in case of a :class:`MultiConfig`, should be :const:`None` for a normal :class:`Config` instance
		:return: A str representation to be written to the config file

		Convert the value of the :class:`Config` instance into a str with :meth:`Config.format_value`.
		'''
		return instance.format_value(config_id)

	def write_help(self, f: typing.TextIO, instance: Config[typing.Any]) -> None:
		'''
		:param f: The file to write to
		:param instance: The config value to be saved

		Write a comment which explains the meaning and usage of this setting
		based on :meth:`Config.format_allowed_values_or_type` and :attr:`Config.help`.

		Use :attr:`last_name` to write the help only once for all :class:`Config` instances belonging to the same :class:`DictConfig` instance.
		'''
		if instance.parent is not None:
			name = instance.parent.key_prefix
		else:
			name = instance.key
		if name == self.last_name:
			return

		prefix = self.config_file.COMMENT + ' '
		n = '\n'

		f.write(n)
		f.write(prefix + name + n)
		f.write(prefix + '-'*len(name) + n)
		f.write(prefix + instance.format_allowed_values_or_type() + n)
		#if instance.unit:
		#	f.write(prefix + 'unit: %s' % instance.unit + n)
		if isinstance(instance.help, dict):
			for key, val in instance.help.items():
				key_name = instance.format_any_value(key)
				val_name = instance.format_any_value(val)
				f.write(prefix + key_name + ': ' + val_name + n)
		elif isinstance(instance.help, str):
			f.write(prefix + instance.help + n)

		self.last_name = name

	def write_data_types(self, f: typing.TextIO, config_instances: 'Iterable[Config[object]]') -> None:
		'''
		:param f: The file to write to
		:param config_instances: All config values to be saved

		Write comments which explain all non-primitive data types
		occurring in :paramref:`config_instances`
		based on their :attr:`help` attribute.
		'''
		data_types_to_be_explained = set()
		for instance in config_instances:
			t = instance.type if instance.type != list else instance.item_type

			if t in self.primitive_types:
				continue

			if issubclass(t, enum.Enum):
				continue

			if not hasattr(t, 'help'):
				continue

			data_types_to_be_explained.add(t)

		prefix = self.config_file.COMMENT + ' '
		n = '\n'

		if not data_types_to_be_explained:
			return

		name = 'Data types'
		f.write(prefix + name + n)
		f.write(prefix + '-'*len(name) + n)

		for name, t in sorted(((getattr(t, 'type_name', t.__name__), t) for t in data_types_to_be_explained), key=lambda name_type: name_type[0]):
			ln = '- %s' % name
			f.write(prefix + ln + n)
			for ln in self.strip_indentation(t.help.rstrip().lstrip('\n').splitlines()):
				ln = '  ' + ln
				f.write(prefix + ln + n)

	@staticmethod
	def strip_indentation(lines: 'Iterable[str]') -> 'Iterator[str]':
		'''
		Strip the indentation of the first line from all lines.

		:raises AssertionError: if one of the following lines does not start with the same indentation
		'''
		lines = iter(lines)
		ln = next(lines)
		stripped_ln = ln.lstrip()
		yield stripped_ln

		i = len(ln) - len(stripped_ln)
		for ln in lines:
			assert i == 0 or ln[:i].isspace()
			yield ln[i:]


class Include(ConfigFileCommand):

	def run(self, cmd: 'Sequence[str]', **kw: 'Unpack[ParseSplittedLineKwargs]') -> None:
		#TODO: --cwd
		#TODO: --no-reset  (change default behaviour to use load_file instead of load_without_resetting_config_id and restore config_id)
		if len(cmd) != 2:
			raise ParseException('invalid number of arguments, expected exactly one: the file to include')

		fn_imp = cmd[1]
		fn_imp = os.path.expanduser(fn_imp)
		#TODO: assume fn to be the path which would be returned by ConfigFile.save() if fn is None
		fn = kw.get('file_name', None)
		if fn and not os.path.isabs(fn_imp):
			fn_imp = os.path.join(os.path.split(os.path.abspath(fn))[0], fn_imp)

		if os.path.isfile(fn_imp):
			self.config_file.load_without_resetting_config_id(fn_imp)
		else:
			raise ParseException(f'no such file {fn_imp!r}')


class UnknownCommand(ConfigFileCommand):

	name = DEFAULT_COMMAND

	def run(self, splitted_line: 'Sequence[str]', **kw: 'Unpack[ParseSplittedLineKwargs]') -> None:
		raise ParseException('unknown command %r' % splitted_line[0])
