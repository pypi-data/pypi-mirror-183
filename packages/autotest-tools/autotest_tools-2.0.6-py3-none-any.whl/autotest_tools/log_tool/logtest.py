from autotest_tools.log_tool.log_config import init

logger = init()


class LogTest:

    @staticmethod
    def debug(tag, msg):
        """
        打印debug级别日志
        :param tag: 标签
        :param msg: 日志内容
        :return: None
        """
        logger.debug("[{}] {}".format(tag, msg))

    @staticmethod
    def info(tag, msg):
        """
        打印info级别日志
        :param tag: 标签
        :param msg: 日志内容
        :return: None
        """
        logger.info("[{}] {}".format(tag, msg))

    @staticmethod
    def warning(tag, msg):
        """
        打印warning级别日志
        :param tag: 标签
        :param msg: 日志内容
        :return: None
        """
        logger.warning("[{}] {}".format(tag, msg))

    @staticmethod
    def error(tag, msg):
        """
        打印error级别日志
        :param tag: 标签
        :param msg: 日志内容
        :return: None
        """
        logger.error("[{}] {}".format(tag, msg))

    @staticmethod
    def critical(tag, msg):
        """
        打印critical级别日志
        :param tag: 标签
        :param msg: 日志内容
        :return: None
        """
        logger.critical("[{}] {}".format(tag, msg))
