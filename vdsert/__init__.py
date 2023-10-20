import importlib.metadata

import structlog

__version__ = importlib.metadata.version(__name__)


def foo():
    logger = structlog.get_logger()
    logger.info("`foo` is called.")
    return "bar"
