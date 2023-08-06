from selenium.webdriver.support.select import Select

from ats.common.log.log import LogTest
from ats.web_test.selenium.selenium_common.driver import DriverCommon

TAG = "SelectCommon"


class SelectCommon(DriverCommon):

    def __init__(self, driver):
        super().__init__(driver)

    def get_select_element(self, loc):
        """
        获取下拉框元素对象
        :param loc: 元素定位
        :return: 下拉框元素对象
        """
        element = self.browser_locate(loc)
        var = Select(element)
        LogTest.debug(TAG, "Get select object")
        return var

    def get_select_options(self, loc):
        """
        获取下拉框选项
        :param loc: 元素定位
        :return: 下拉框选项
        """
        select = self.get_select_element(loc)
        var = select.options
        LogTest.debug(TAG, "Select options: {}".format(var))
        return var

    def get_selected_options(self, loc):
        """
        获取已被选中的下拉框选项
        :param loc: 元素定位
        :return: 已被选中的下拉框选项
        """
        select = self.get_select_element(loc)
        var = select.all_selected_options
        LogTest.debug(TAG, "All selected options: {}".format(var))
        return var

    def get_first_selected_option(self, loc):
        """
        获取第一个已被选中的下拉框选项
        :param loc: 元素定位
        :return: 第一个已被选中的下拉框选项
        """
        select = self.get_select_element(loc)
        var = select.first_selected_option
        LogTest.debug(TAG, "First selected option: {}".format(var))
        return var

    def select_by_value(self, loc, value):
        """
        通过value选择下拉框选项
        :param loc: 元素定位
        :param value: value
        :return: None
        """
        select = self.get_select_element(loc)
        select.select_by_value(value)
        LogTest.debug(TAG, "Select by value: {}".format(value))
        return None

    def select_by_index(self, loc, index):
        """
        通过index选择下拉框选项
        :param loc: 元素定位
        :param index: index
        :return: None
        """
        select = self.get_select_element(loc)
        select.select_by_index(index)
        LogTest.debug(TAG, "Select by index: {}".format(index))
        return None

    def select_by_visible_text(self, loc, text):
        """
        通过index选择下拉框选项
        :param loc: 元素定位
        :param text: text
        :return: None
        """
        select = self.get_select_element(loc)
        select.select_by_visible_text(text)
        LogTest.debug(TAG, "Select by text: {}".format(text))
        return None

    def deselect_all(self, loc):
        """
        取消所有选择
        :param loc: 元素定位
        :return: None
        """
        select = self.get_select_element(loc)
        select.deselect_all()
        LogTest.debug(TAG, "Deselect all")
        return None

    def deselect_by_value(self, loc, value):
        """
        通过value取消选择下拉框选项
        :param loc: 元素定位
        :param value: value
        :return: None
        """
        select = self.get_select_element(loc)
        select.deselect_by_value(value)
        LogTest.debug(TAG, "Deselect by value: {}".format(value))
        return None

    def deselect_by_index(self, loc, index):
        """
        通过index取消选择下拉框选项
        :param loc: 元素定位
        :param index: index
        :return: None
        """
        select = self.get_select_element(loc)
        select.deselect_by_index(index)
        LogTest.debug(TAG, "Deselect by index: {}".format(index))
        return None

    def deselect_by_visible_text(self, loc, text):
        """
        通过index取消选择下拉框选项
        :param loc: 元素定位
        :param text: text
        :return: None
        """
        select = self.get_select_element(loc)
        select.deselect_by_visible_text(text)
        LogTest.debug(TAG, "Deselect by text: {}".format(text))
        return None
