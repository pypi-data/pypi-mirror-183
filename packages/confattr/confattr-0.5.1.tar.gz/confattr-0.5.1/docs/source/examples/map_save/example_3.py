#!../../../../venv/bin/python3
import os
os.environ['XDG_CONFIG_HOME'] = os.path.dirname(__file__)

# ------- start -------
import argparse
from collections.abc import Sequence
import typing

import urwid
from confattr import ConfigFileArgparseCommand, ConfigFile

if typing.TYPE_CHECKING:
	from typing_extensions import Unpack  # This will hopefully be replaced by the ** syntax proposed in https://peps.python.org/pep-0692/
	from confattr import SaveKwargs

	class MapSaveKwargs(SaveKwargs, total=False):
		urwid_commands: 'Sequence[str]'

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

	def save(self, f: typing.TextIO, **kw: 'Unpack[MapSaveKwargs]') -> None:
		commands = kw.get('urwid_commands', sorted(urwid.command_map._command.values()))
		for cmd in commands:
			for key in urwid.command_map._command.keys():
				if urwid.command_map[key] == cmd:
					quoted_key = self.config_file.quote(key)
					quoted_cmd = self.config_file.quote(cmd)
					print(f'map {quoted_key} {quoted_cmd}', file=f)


if __name__ == '__main__':
	urwid_commands = [urwid.CURSOR_UP, urwid.CURSOR_DOWN, urwid.ACTIVATE, 'confirm']
	mapkw: 'MapSaveKwargs' = dict(urwid_commands=urwid_commands)
	kw: 'SaveKwargs' = mapkw
	config_file = ConfigFile(appname=__package__)
	config_file.save(**kw)
