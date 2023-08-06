import logging

import colorlog

TAG = "LogTest"


def init():
    """
    初始化日志
    :return: None
    """
    logger = logging.getLogger(TAG)
    logger.setLevel(logging.DEBUG)
    console_formatter = colorlog.ColoredFormatter(
        fmt="%(log_color)s %(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S")

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    return logger
