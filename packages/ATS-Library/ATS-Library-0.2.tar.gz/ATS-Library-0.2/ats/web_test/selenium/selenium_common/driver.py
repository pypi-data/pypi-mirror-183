from selenium.webdriver.remote.webelement import WebElement

from ats.common.log.log import LogTest

TAG = "DriverCommon"


class DriverCommon(object):

    def __init__(self, driver):
        self.driver = driver

    def get_browser_name(self):
        """
        获取浏览器名称
        :return: 浏览器名称
        """
        var = self.driver.name
        LogTest.debug(TAG, "Browser name is: {}".format(var))
        return var

    def open_url(self, url):
        """
        打开网页
        :param url: 网页地址
        :return: None
        """
        LogTest.debug(TAG, "Visit url: {}".format(url))
        self.driver.get(url)
        return None

    def get_page_title(self):
        """
        获取网页标题
        :return: 网页标题
        """
        var = self.driver.title
        LogTest.debug(TAG, "Page title is: {}".format(var))
        return var

    def execute_js(self, script, *args):
        """
        执行js脚本
        :param script: js脚本
        :param args: 参数
        :return: 执行结果
        """
        var = self.driver.execute_script(script, *args)
        LogTest.debug(TAG, "Execute js script: {}".format(script))
        return var

    def execute_async_js(self, script, *args):
        """
        执行异步js脚本
        :param script: js脚本
        :param args: 参数
        :return: 执行结果
        """
        var = self.driver.execute_async_script(script, *args)
        LogTest.debug(TAG, "Execute async js script: {}".format(script))
        return var

    def get_current_url(self):
        """
        获取当前网页地址
        :return: 网页地址
        """
        var = self.driver.current_url
        LogTest.debug(TAG, "Current url is: {}".format(var))
        return var

    def get_page_source(self):
        """
        获取网页源码
        :return: 网页源码
        """
        var = self.driver.page_source
        LogTest.debug(TAG, "Get page source: {}".format(var))
        return var

    def close_browser(self):
        """
        关闭浏览器
        :return: None
        """
        LogTest.debug(TAG, "Close browser")
        self.driver.close()
        return None

    def quit_browser(self):
        """
        退出浏览器
        :return: None
        """
        LogTest.debug(TAG, "Quit browser")
        self.driver.quit()
        return None

    def get_current_window_handle(self):
        """
        获取当前窗口句柄
        :return: 窗口句柄
        """
        var = self.driver.current_window_handle
        LogTest.debug(TAG, "Current window handle is: {}".format(var))
        return var

    def get_window_handles(self):
        """
        获取所有窗口句柄
        :return: 窗口句柄列表
        """
        var = self.driver.window_handles
        LogTest.debug(TAG, "Window handles is: {}".format(var))
        return var

    def maximize_window(self):
        """
        最大化窗口
        :return: None
        """
        LogTest.debug(TAG, "Maximize window")
        self.driver.maximize_window()
        return None

    def minimize_window(self):
        """
        最小化窗口
        :return: None
        """
        LogTest.debug(TAG, "Minimize window")
        self.driver.minimize_window()
        return None

    def full_screen_window(self):
        """
        全屏窗口
        :return: None
        """
        LogTest.debug(TAG, "Full screen window")
        self.driver.fullscreen_window()
        return None

    def print_page(self):
        """
        打印网页
        :return: None
        """
        var = self.driver.print_page()
        LogTest.debug(TAG, "Print page: {}".format(var))
        return var

    def switch_to_active_element(self):
        """
        切换到活动元素
        :return: 活动元素
        """
        var = self.driver.switch_to.active_element
        LogTest.debug(TAG, "Switch to active element: {}".format(var))
        return var

    def switch_to_alert(self):
        """
        切换到警告框
        :return: alert
        """
        var = self.driver.switch_to.alert
        LogTest.debug(TAG, "Switch to alert: {}".format(var))
        return var

    def switch_to_default_content(self):
        """
        切换回默认内容
        :return: None
        """
        LogTest.debug(TAG, "Switch to default content")
        self.driver.switch_to.default_content()
        return None

    def switch_to_frame(self, frame_reference):
        """
        切换到iframe
        :param frame_reference: iframe
        :return: None
        """
        LogTest.debug(TAG, "Switch to frame: {}".format(frame_reference))
        self.driver.switch_to.frame(frame_reference)
        return None

    def switch_to_parent_frame(self):
        """
        切换到父iframe
        :return: None
        """
        LogTest.debug(TAG, "Switch to parent frame")
        self.driver.switch_to.parent_frame()
        return None

    def switch_to_window(self, window_name):
        """
        切换到窗口
        :param window_name: 窗口名称
        :return: None
        """
        LogTest.debug(TAG, "Switch to window: {}".format(window_name))
        self.driver.switch_to.window(window_name)
        return None

    def go_back(self):
        """
        后退
        :return: None
        """
        LogTest.debug(TAG, "Go back")
        self.driver.back()
        return None

    def go_forward(self):
        """
        前进
        :return: None
        """
        LogTest.debug(TAG, "Go forward")
        self.driver.forward()
        return None

    def refresh_browser(self):
        """
        刷新
        :return: None
        """
        LogTest.debug(TAG, "Refresh browser")
        self.driver.refresh()
        return None

    def get_cookies(self):
        """
        获取所有的cookie
        :return: cookies
        """
        var = self.driver.get_cookies()
        LogTest.debug(TAG, "Get cookies: {}".format(var))
        return var

    def get_cookie(self, name):
        """
        获取cookie
        :param name: cookie名称
        :return: cookie
        """
        var = self.driver.get_cookie(name)
        LogTest.debug(TAG, "Get cookie: {}".format(var))
        return var

    def add_cookie(self, cookie_dict):
        """
        添加cookie
        :param cookie_dict: cookie字典
        :return: None
        """
        LogTest.debug(TAG, "Add cookie: {}".format(cookie_dict))
        self.driver.add_cookie(cookie_dict)
        return None

    def delete_cookie(self, name):
        """
        删除cookie
        :param name: cookie名称
        :return: None
        """
        LogTest.debug(TAG, "Delete cookie: {}".format(name))
        self.driver.delete_cookie(name)
        return None

    def delete_all_cookies(self):
        """
        删除所有cookie
        :return: None
        """
        LogTest.debug(TAG, "Delete all cookies")
        self.driver.delete_all_cookies()
        return None

    def set_implicitly_wait(self, seconds):
        """
        设置隐式等待时间
        :param seconds: 秒
        :return: None
        """
        LogTest.debug(TAG, "Set implicitly wait: {}s".format(seconds))
        self.driver.implicitly_wait(seconds)
        return None

    def set_script_timeout(self, seconds):
        """
        设置脚本超时时间
        :param seconds: 秒
        :return: None
        """
        LogTest.debug(TAG, "Set script timeout: {}s".format(seconds))
        self.driver.set_script_timeout(seconds)
        return None

    def set_page_load_timeout(self, seconds):
        """
        设置页面加载超时时间
        :param seconds: 秒
        :return: None
        """
        LogTest.debug(TAG, "Set page load timeout: {}s".format(seconds))
        self.driver.set_page_load_timeout(seconds)
        return None

    def get_timeout(self):
        """
        获取超时时间
        :return: 超时时间
        """
        var = self.driver.timeouts
        LogTest.debug(TAG, "Get timeout: {}".format(var))
        return var

    def browser_locate(self, loc):
        """
        浏览器定位
        :param loc: 定位
        :return: 定位元素
        """
        LogTest.debug(TAG, "Browser locate: {}".format(loc))

        def _func(_loc):
            elements = self.driver.find_elements(*_loc)
            if 1 == len(elements):
                return elements[0]
            return elements

        if isinstance(loc, tuple):
            loc = _func(loc)
        elif isinstance(loc, WebElement):
            pass
        else:
            LogTest.error(TAG, "Loc must be tuple or WebElement")
            raise TypeError("loc must be tuple or WebElement")
        return loc

    def get_desired_capabilities(self):
        """
        获取当前浏览器驱动配置
        :return: 浏览器配置
        """
        var = self.driver.desired_capabilities
        LogTest.debug(TAG, "Get desired capabilities: {}".format(var))
        return var

    def get_capabilities(self):
        """
        获取浏览器驱动配置
        :return: 浏览器配置
        """
        var = self.driver.capabilities
        LogTest.debug(TAG, "Get capabilities: {}".format(var))
        return var

    def get_browser_screenshot_as_file(self, filename):
        """
        获取浏览器截图并保存
        :param filename: 文件名
        :return: None
        """
        LogTest.debug(TAG, "Get browser screenshot as file: {}".format(filename))
        self.driver.get_screenshot_as_file(filename)
        return None

    def get_browser_screenshot_as_png(self):
        """
        获取浏览器截图二进制数据
        :return: 截图
        """
        var = self.driver.get_screenshot_as_png()
        LogTest.debug(TAG, "Get browser screenshot as png")
        return var

    def get_browser_screenshot_as_base64(self):
        """
        获取浏览器截图base64编码
        :return: 截图
        """
        var = self.driver.get_screenshot_as_base64()
        LogTest.debug(TAG, "Get browser screenshot as base64")
        return var

    def save_screenshot(self, filename):
        """
        保存截图
        :param filename: 文件名
        :return: None
        """
        LogTest.debug(TAG, "Save screenshot: {}".format(filename))
        self.driver.save_screenshot(filename)
        return None

    def set_window_size(self, width, height):
        """
        设置窗口大小
        :param width: 宽度
        :param height: 高度
        :return: None
        """
        LogTest.debug(TAG, "Set window size: {}x{}".format(width, height))
        self.driver.set_window_size(width, height)
        return None

    def get_window_size(self):
        """
        获取窗口大小
        :return: 窗口大小
        """
        var = self.driver.get_window_size()
        LogTest.debug(TAG, "Get window size: {}".format(var))
        return var

    def set_window_position(self, x, y):
        """
        设置窗口位置
        :param x: x坐标
        :param y: y坐标
        :return: None
        """
        LogTest.debug(TAG, "Set window position: {},{}".format(x, y))
        self.driver.set_window_position(x, y)
        return None

    def get_window_position(self):
        """
        获取窗口位置
        :return: 窗口位置
        """
        var = self.driver.get_window_position()
        LogTest.debug(TAG, "Get window position: {}".format(var))
        return var

    def get_window_rect(self):
        """
        获取窗口位置和大小
        :return: 窗口位置和大小
        """
        var = self.driver.get_window_rect()
        LogTest.debug(TAG, "Get window rect: {}".format(var))
        return var

    def set_window_rect(self, x, y, width, height):
        """
        设置窗口位置和大小
        :param x: x坐标
        :param y: y坐标
        :param width: 宽度
        :param height: 高度
        :return: None
        """
        LogTest.debug(TAG, "Set window rect: {},{},{}x{}".format(x, y, width, height))
        self.driver.set_window_rect(x, y, width, height)
        return None

    def get_orientation(self):
        """
        获取屏幕方向
        :return: 屏幕方向
        """
        var = self.driver.orientation
        LogTest.debug(TAG, "Get orientation: {}".format(var))
        return var

    def get_application_cache(self):
        """
        获取应用缓存
        :return: 应用缓存
        """
        var = self.driver.application_cache
        LogTest.debug(TAG, "Get application cache: {}".format(var))
        return var

    def get_log_types(self):
        """
        获取浏览器日志类型
        :return: 日志类型
        """
        var = self.driver.log_types
        LogTest.debug(TAG, "Get log types: {}".format(var))
        return var

    def get_browser_log(self, log_type):
        """
        获取浏览器日志
        :param log_type: 日志类型
        :return: 日志
        """
        var = self.driver.get_log(log_type)
        LogTest.debug(TAG, "Get browser log: {}".format(var))
        return var
