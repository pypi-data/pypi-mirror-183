from ats.web_test.selenium.selenium_common.alert import AlertCommon
from ats.web_test.selenium.selenium_common.ec import EcCommon
from ats.web_test.selenium.selenium_common.element import ElementCommon
from ats.web_test.selenium.selenium_common.keyboard import KeyboardCommon
from ats.web_test.selenium.selenium_common.mouse import MouseCommon
from ats.web_test.selenium.selenium_common.select import SelectCommon
from ats.web_test.selenium.selenium_common.ui import UiCommon
from ats.web_test.selenium.selenium_common.wait import WaitCommon


class BasePage(AlertCommon,
               EcCommon,
               ElementCommon,
               KeyboardCommon,
               MouseCommon,
               SelectCommon,
               UiCommon,
               WaitCommon):
    ...
