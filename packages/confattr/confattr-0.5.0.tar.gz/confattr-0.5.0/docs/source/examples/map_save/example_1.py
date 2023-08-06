#!../../../../venv/bin/python3
import os
os.environ['XDG_CONFIG_HOME'] = os.path.dirname(__file__)

# ------- start -------
import argparse
import typing
if typing.TYPE_CHECKING:
	from typing_extensions import Unpack  # This will hopefully be replaced by the ** syntax proposed in https://peps.python.org/pep-0692/
	from confattr import SaveKwargs

import urwid
from confattr import ConfigFileArgparseCommand, ConfigFile


class Map(ConfigFileArgparseCommand):

	'''
	bind a command to a key
	'''

	@classmethod
	def init_parser(cls) -> None:
		cls.parser.add_argument('key', help='http://urwid.org/manual/userinput.html#keyboard-input')
		cls.parser.add_argument('cmd', help='any urwid command')

	def run_parsed(self, args: argparse.Namespace) -> None:
		urwid.command_map[args.key] = args.cmd

	def save(self, f: typing.TextIO, **kw: 'Unpack[SaveKwargs]') -> None:
		for key, cmd in sorted(urwid.command_map._command.items(), key=lambda key_cmd: str(key_cmd[1])):
			quoted_key = self.config_file.quote(key)
			quoted_cmd = self.config_file.quote(cmd)
			print(f'map {quoted_key} {quoted_cmd}', file=f)


if __name__ == '__main__':
	ConfigFile(appname=__package__).save()
