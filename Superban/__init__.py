from Superban.core.dir import dirr
from Superban.core.bot import app
from Superban.core.bot import start_bot

from .logging import LOGGER

dirr()

__all__ = ["app", "start_bot"]