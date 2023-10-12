import structlog

version = "1.1.0"


def foo():
    logger = structlog.get_logger()
    logger.info("`foo` is called.")
    return "bar"
