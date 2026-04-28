# logger/__init__.py
from .logger import Logger
# Create a single shared logger instance
GLOBAL_LOGGER = Logger().get_logger("movie_ai")