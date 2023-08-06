from typing import Any, List, Tuple

import logging

logging.basicConfig(
    filename="config.log",
    filemode="w",
    level=logging.INFO,
    format="%(name)s - %(levelname)s - %(message)s",
)


class Config:
    def __init__(self) -> None:
        self.CONF_DEBUG: bool = True
        self.GOOGLE_API_KEY: str = ""


# General
CONF_DEBUG = True
# Google
GOOGLE_API_KEY = ""
GOOGLE_SEARCH_ENGINE_ID = ""
# NLP
NLP_CONF_MODE = "default"

"""
class Config:

    def __init__(self: Any) -> None:
        self.CONF_DEBUG: str = True
        self.GOOGLE_API_KEY: str = ""
        self.GOOGLE_SEARCH_ENGINE_ID: str = ""
        self.NLP_CONF_MODE: str = "default"

    def google_config(self: Any, GOOGLE_API_KEY: str, GOOGLE_SEARCH_ENGINE_ID: str) -> None:
        self.GOOGLE_API_KEY = GOOGLE_API_KEY
        self.GOOGLE_SEARCH_ENGINE_ID = GOOGLE_SEARCH_ENGINE_ID
"""


def NLP_config(mode: str = "default", debug: bool = True) -> None:
    global NLP_CONF_MODE, CONF_DEBUG
    CONF_DEBUG = debug
    if mode == "accuracy" or mode == "speed":
        NLP_CONF_MODE = mode
    else:
        if CONF_DEBUG:
            logging.warn(f"mode: {mode} does not exist")
