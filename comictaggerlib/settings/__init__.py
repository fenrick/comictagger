from __future__ import annotations

from comictaggerlib.settings.cmdline import initial_cmd_line_parser, register_commandline, validate_commandline_options
from comictaggerlib.settings.file import register_settings, validate_settings
from comictaggerlib.settings.manager import Manager, OptionDefinitions, OptionValues, defaults, save_file
from comictaggerlib.settings.types import ComicTaggerPaths

__all__ = [
    "initial_cmd_line_parser",
    "register_commandline",
    "register_settings",
    "validate_commandline_options",
    "validate_settings",
    "Manager",
    "ComicTaggerPaths",
    "OptionValues",
    "OptionDefinitions",
    "save_file",
    "defaults",
]
