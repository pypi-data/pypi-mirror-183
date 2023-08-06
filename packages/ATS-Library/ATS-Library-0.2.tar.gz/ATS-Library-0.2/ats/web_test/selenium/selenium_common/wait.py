import time

from ats.common.log.log import LogTest
from ats.web_test.selenium.selenium_common.driver import DriverCommon

TAG = "WaitTool"


class WaitCommon(DriverCommon):

    def __init__(self, driver):
        super().__init__(driver)

    def wait(self, seconds):
        """
        等待
        :param seconds: 秒数
        :return: None
        """
        LogTest.debug(TAG, "Wait for {} seconds".format(seconds))
        time.sleep(seconds)
