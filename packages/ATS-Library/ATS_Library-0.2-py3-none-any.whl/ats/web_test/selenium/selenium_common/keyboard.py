from selenium.webdriver import ActionChains, Keys

from ats.common.log.log import LogTest
from ats.web_test.selenium.selenium_common.driver import DriverCommon

TAG = "KeyboardCommon"


class KeyboardCommon(DriverCommon):

    def __init__(self, driver):
        super().__init__(driver)
        self.keyboard = ActionChains(self.driver)

    def keyboard_reset(self):
        """
        重置键盘
        :return: None
        """
        LogTest.debug(TAG, "Reset keyboard")
        self.keyboard.reset_actions()
        return None

    def keyboard_down(self, key):
        """
        按下某个键
        :param key: 键名
        :return: None
        """
        LogTest.debug(TAG, "Press down key: {}".format(key))
        self.keyboard_reset()
        self.keyboard.key_down(key)
        self.keyboard.perform()
        return None

    def keyboard_up(self, key):
        """
        松开某个键
        :param key: 键名
        :return: None
        """
        LogTest.debug(TAG, "Release key: {}".format(key))
        self.keyboard_reset()
        self.keyboard.key_up(key)
        self.keyboard.perform()
        return None

    def keyboard_press(self, key):
        """
        按下某个键并松开
        :param key: 键名
        :return: None
        """
        LogTest.debug(TAG, "Press key and release: {}".format(key))
        self.keyboard_reset()
        self.keyboard.key_down(key).key_up(key)
        self.keyboard.perform()
        return None

    def keyboard_pause(self, seconds):
        """
        键盘暂停
        :param seconds: 秒数
        :return: None
        """
        LogTest.debug(TAG, "Keyboard pause {} seconds".format(seconds))
        self.keyboard_reset()
        self.keyboard.pause(seconds)
        self.keyboard.perform()
        return None

    def keyboard_release(self):
        """
        释放键盘
        :return: None
        """
        LogTest.debug(TAG, "Release keyboard")
        self.keyboard_reset()
        self.keyboard.release()
        self.keyboard.perform()
        return None

    def keyboard_press_enter(self):
        """
        按下回车键
        :return: None
        """
        LogTest.debug(TAG, "Press enter key")
        self.keyboard_press(Keys.ENTER)
        return None

    def keyboard_press_tab(self):
        """
        按下Tab键
        :return: None
        """
        LogTest.debug(TAG, "Press tab key")
        self.keyboard_press(Keys.TAB)
        return None

    def keyboard_press_space(self):
        """
        按下空格键
        :return: None
        """
        LogTest.debug(TAG, "Press space key")
        self.keyboard_press(Keys.SPACE)
        return None

    def keyboard_press_escape(self):
        """
        按下Esc键
        :return: None
        """
        LogTest.debug(TAG, "Press escape key")
        self.keyboard_press(Keys.ESCAPE)
        return None

    def keyboard_press_backspace(self):
        """
        按下Backspace键
        :return: None
        """
        LogTest.debug(TAG, "Press backspace key")
        self.keyboard_press(Keys.BACKSPACE)
        return None

    def keyboard_press_delete(self):
        """
        按下Delete键
        :return: None
        """
        LogTest.debug(TAG, "Press delete key")
        self.keyboard_press(Keys.DELETE)
        return None

    def keyboard_press_control(self):
        """
        按下Ctrl键
        :return: None
        """
        LogTest.debug(TAG, "Press control key")
        self.keyboard_press(Keys.CONTROL)
        return None

    def keyboard_press_alt(self):
        """
        按下Alt键
        :return: None
        """
        LogTest.debug(TAG, "Press alt key")
        self.keyboard_press(Keys.ALT)
        return None

    def keyboard_press_shift(self):
        """
        按下Shift键
        :return: None
        """
        LogTest.debug(TAG, "Press shift key")
        self.keyboard_press(Keys.SHIFT)
        return None

    def keyboard_ctrl_a(self, loc):
        """
        Ctrl+A
        :param loc: 元素定位
        :return: None
        """
        LogTest.debug(TAG, "Press ctrl+a")
        element = self.browser_locate(loc)
        element.send_keys(Keys.CONTROL, "a")
        return None

    def keyboard_ctrl_c(self, loc):
        """
        Ctrl+C
        :param loc: 元素定位
        :return: None
        """
        LogTest.debug(TAG, "Press ctrl+c")
        element = self.browser_locate(loc)
        element.send_keys(Keys.CONTROL, "c")
        return None

    def keyboard_ctrl_v(self, loc):
        """
        Ctrl+V
        :param loc: 元素定位
        :return: None
        """
        LogTest.debug(TAG, "Press ctrl+v")
        element = self.browser_locate(loc)
        element.send_keys(Keys.CONTROL, "v")
        return None

    def keyboard_ctrl_x(self, loc):
        """
        Ctrl+X
        :param loc: 元素定位
        :return: None
        """
        LogTest.debug(TAG, "Press ctrl+x")
        element = self.browser_locate(loc)
        element.send_keys(Keys.CONTROL, "x")
        return None

    def keyboard_ctrl_z(self, loc):
        """
        Ctrl+Z
        :param loc: 元素定位
        :return: None
        """
        LogTest.debug(TAG, "Press ctrl+z")
        element = self.browser_locate(loc)
        element.send_keys(Keys.CONTROL, "z")
        return None

    def keyboard_ctrl_s(self, loc):
        """
        Ctrl+S
        :param loc: 元素定位
        :return: None
        """
        LogTest.debug(TAG, "Press ctrl+s")
        element = self.browser_locate(loc)
        element.send_keys(Keys.CONTROL, "s")
        return None

    def keyboard_ctrl_f(self, loc):
        """
        Ctrl+F
        :param loc: 元素定位
        :return: None
        """
        LogTest.debug(TAG, "Press ctrl+f")
        element = self.browser_locate(loc)
        element.send_keys(Keys.CONTROL, "f")
        return None
