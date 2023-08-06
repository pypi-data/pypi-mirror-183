from selenium.common import NoAlertPresentException


from ats.common.log.log import LogTest
from ats.web_test.selenium.selenium_common.driver import DriverCommon

TAG = "AlertCommon"


class AlertCommon(DriverCommon):

    def __init__(self, driver):
        super().__init__(driver)
        self.alert = None

    def get_alert_text(self):
        """
        获取警告框的文本信息
        :return: 警告框的文本信息
        """
        self.alert = self.driver.switch_to_alert()
        var = self.alert.text
        LogTest.debug(TAG, "Get alert text, text is: {}".format(var))
        return var

    def alert_accept(self):
        """
        接受警告框
        :return: None
        """
        LogTest.debug(TAG, "Accept alert")
        self.alert = self.driver.switch_to_alert()
        self.alert.accept()
        return None

    def alert_dismiss(self):
        """
        取消警告框
        :return: None
        """
        LogTest.debug(TAG, "Dismiss alert")
        self.alert = self.driver.switch_to_alert()
        self.alert.dismiss()
        return None

    def alert_send_keys(self, text):
        """
        输入文本到警告框
        :param text: 输入的文本
        :return: None
        """
        LogTest.debug(TAG, "Input text to alert, text is: {}".format(text))
        self.alert = self.driver.switch_to_alert()
        self.alert.send_keys(text)
        return None

    def is_alert_exist(self):
        """
        判断警告框是否存在
        :return: True or False
        """
        try:
            self.driver.switch_to_alert()
            LogTest.debug(TAG, "Alert is exist")
            return True
        except NoAlertPresentException:
            LogTest.error(TAG, "Alert is not exist")
            return False

    def is_alert_exist_accept(self):
        """
        判断警告框是否存在，存在则接受
        :return: None
        """
        if self.is_alert_exist():
            LogTest.debug(TAG, "Alert is exist, accept")
            self.alert_accept()
        return None

    def is_alert_exist_dismiss(self):
        """
        判断警告框是否存在，存在则取消
        :return: None
        """
        if self.is_alert_exist():
            LogTest.debug(TAG, "Alert is exist, dismiss")
            self.alert_dismiss()
        return None

    def is_alert_exist_send_keys(self, text):
        """
        判断警告框是否存在，存在则输入文本
        :param text: 输入的文本
        :return: None
        """
        if self.is_alert_exist():
            LogTest.debug(TAG, "Alert is exist, input text to alert, text is: {}".format(text))
            self.alert_send_keys(text)
        return None

    def is_alert_exist_get_text(self):
        """
        判断警告框是否存在，存在则获取文本信息
        :return: 警告框的文本信息
        """
        if self.is_alert_exist():
            var = self.get_alert_text()
            LogTest.debug(TAG, "Alert is exist, get alert text, text is: {}".format(var))
            return var
        return None
