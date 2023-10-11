import structlog


def foo():
    logger = structlog.get_logger()
    logger.info("`foo` is called.")
    return "bar"
