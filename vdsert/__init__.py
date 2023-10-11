import structlog

version = "0.2.0"


def foo():
    logger = structlog.get_logger()
    logger.info("`foo` is called.")
    return "bar"
