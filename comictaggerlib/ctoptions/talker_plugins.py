from __future__ import annotations

import logging

import settngs

from comictalker.comictalkerapi import TalkerPlugin

logger = logging.getLogger(__name__)


def register_talker_settings(parser: settngs.Manager, plugins: dict[str, TalkerPlugin]) -> None:
    for talker_name, talker in plugins.items():
        try:
            parser.add_group(talker_name, talker["cls"].comic_settings, False)
        except Exception:
            logger.exception("Failed to register settings for %s", talker_name)
