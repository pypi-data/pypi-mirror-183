from ats.common.log.config import init

log = init()


class LogTest:

    @staticmethod
    def debug(tag, msg):
        """
        打印debug级别日志
        :param tag: 标签
        :param msg: 日志内容
        :return: None
        """
        log.debug("[{}] {}".format(tag, msg))

    @staticmethod
    def info(tag, msg):
        """
        打印info级别日志
        :param tag: 标签
        :param msg: 日志内容
        :return: None
        """
        log.info("[{}] {}".format(tag, msg))

    @staticmethod
    def warning(tag, msg):
        """
        打印warning级别日志
        :param tag: 标签
        :param msg: 日志内容
        :return: None
        """
        log.warning("[{}] {}".format(tag, msg))

    @staticmethod
    def error(tag, msg):
        """
        打印error级别日志
        :param tag: 标签
        :param msg: 日志内容
        :return: None
        """
        log.error("[{}] {}".format(tag, msg))

    @staticmethod
    def critical(tag, msg):
        """
        打印critical级别日志
        :param tag: 标签
        :param msg: 日志内容
        :return: None
        """
        log.critical("[{}] {}".format(tag, msg))
