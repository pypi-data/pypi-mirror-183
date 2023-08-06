import platform

from selenium import webdriver

from ats.common.log.log import LogTest

TAG = "BrowserCommon"


class BrowserCommon(object):

    @staticmethod
    def init_browser(grid=None, option=None):
        """
        获取浏览器驱动
        :param grid: grid地址
        :param option: Chrome option设置
        :return: 浏览器驱动
        """
        LogTest.debug(TAG, "Init browser")
        options = webdriver.ChromeOptions()
        for _ in option:
            options.add_argument(_)
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        if platform.system() == "Linux":
            browser = webdriver.Remote(command_executor=grid, options=options)
        else:
            browser = webdriver.Chrome(options=options)
            browser.maximize_window()
        browser.implicitly_wait(3.5)
        browser.set_page_load_timeout(10.0)
        return browser
