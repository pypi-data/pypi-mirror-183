import time

from ats.common.log.log import LogTest

TAG = "TimeCommon"


class TimeCommon(object):

    @staticmethod
    def get_stamp():
        """
        获取当前时间戳
        :return: 当前时间戳
        """
        time_stamp = time.time()
        LogTest.debug(TAG, "Get time stamp: {}".format(time_stamp))
        return time_stamp

    @staticmethod
    def get_localtime():
        """
        获取当前时间
        :return: 当前时间
        """
        time_stamp = TimeCommon.get_stamp()
        localtime = time.localtime(time_stamp)
        LogTest.debug(TAG, "Get local time: {}".format(localtime))
        return localtime

    @staticmethod
    def get_format_time(time_format):
        """
        获取当前时间并以指定格式返回
        :param time_format: 时间格式
        :return: 当前时间
        """
        localtime = TimeCommon.get_localtime()
        format_time = time.strftime(time_format, localtime)
        LogTest.debug(TAG, "Get format time: {}".format(format_time))
        return format_time
