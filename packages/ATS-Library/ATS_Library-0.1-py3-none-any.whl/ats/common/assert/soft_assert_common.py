from ats.common.log.log import LogTest

TAG = "SoftAssert"


class SoftAssert(object):

    def __init__(self):
        self._verificationErrors = []

    def verify_equal(self, actual, expected, message=None):
        """
        软断言相等
        :param actual: 实际值
        :param expected: 期望值
        :param message: 描述信息
        :return: None
        """
        LogTest.debug(TAG, "VerifyEqual: actual = {}, expected = {}".format(actual, expected))
        try:
            assert actual == expected
        except AssertionError:
            LogTest.error(TAG, "VerifyEqual Failed: actual = {}, expected = {}".format(actual, expected))
            self._verificationErrors.append(message)

    def verify_not_equal(self, actual, expected, message=None):
        """
        软断言不相等
        :param actual: 实际值
        :param expected: 期望值
        :param message: 描述信息
        :return: None
        """
        LogTest.debug(TAG, "VerifyNotEqual: actual = {}, expected = {}".format(actual, expected))
        try:
            assert actual != expected
        except AssertionError:
            LogTest.error(TAG, "VerifyNotEqual Failed: actual = {}, expected = {}".format(actual, expected))
            self._verificationErrors.append(message)

    def verify_true(self, condition, message=None):
        """
        软断言条件为真
        :param condition: 条件
        :param message: 描述信息
        :return: None
        """
        LogTest.debug(TAG, "VerifyTrue: condition = {}".format(condition))
        try:
            assert condition
        except AssertionError:
            LogTest.error(TAG, "VerifyTrue Failed: condition = {}".format(condition))
            self._verificationErrors.append(message)

    def verify_false(self, condition, message=None):
        """
        软断言条件为假
        :param condition: 条件
        :param message: 描述信息
        :return: None
        """
        LogTest.debug(TAG, "VerifyFalse: condition = {}".format(condition))
        try:
            assert not condition
        except AssertionError:
            LogTest.error(TAG, "VerifyFalse Failed: condition = {}".format(condition))
            self._verificationErrors.append(message)

    def verify_in(self, member, container, message=None):
        """
        软断言成员存在于容器中
        :param member: 成员
        :param container: 容器
        :param message: 描述信息
        :return: None
        """
        LogTest.debug(TAG, "VerifyIn: member = {}, container = {}".format(member, container))
        try:
            assert member in container
        except AssertionError:
            LogTest.error(TAG, "VerifyIn Failed: member = {}, container = {}".format(member, container))
            self._verificationErrors.append(message)

    def verify_not_in(self, member, container, message=None):
        """
        软断言成员不存在于容器中
        :param member: 成员
        :param container: 容器
        :param message: 描述信息
        :return: None
        """
        LogTest.debug(TAG, "VerifyNotIn: member = {}, container = {}".format(member, container))
        try:
            assert member not in container
        except AssertionError:
            LogTest.error(TAG, "VerifyNotIn Failed: member = {}, container = {}".format(member, container))
            self._verificationErrors.append(message)

    def verify_is(self, expr1, expr2, message=None):
        """
        软断言两个表达式引用同一个对象
        :param expr1: 表达式1
        :param expr2: 表达式2
        :param message: 描述信息
        :return: None
        """
        LogTest.debug(TAG, "VerifyIs: expr1 = {}, expr2 = {}".format(expr1, expr2))
        try:
            assert expr1 is expr2
        except AssertionError:
            LogTest.error(TAG, "VerifyIs Failed: expr1 = {}, expr2 = {}".format(expr1, expr2))
            self._verificationErrors.append(message)

    def verify_is_not(self, expr1, expr2, message=None):
        """
        软断言两个表达式引用不同的对象
        :param expr1: 表达式1
        :param expr2: 表达式2
        :param message: 描述信息
        :return: None
        """
        LogTest.debug(TAG, "VerifyIsNot: expr1 = {}, expr2 = {}".format(expr1, expr2))
        try:
            assert expr1 is not expr2
        except AssertionError:
            LogTest.error(TAG, "VerifyIsNot Failed: expr1 = {}, expr2 = {}".format(expr1, expr2))
            self._verificationErrors.append(message)

    def verify_is_none(self, obj, message=None):
        """
        软断言对象为None
        :param obj: 对象
        :param message: 描述信息
        :return: None
        """
        LogTest.debug(TAG, "VerifyIsNone: obj = {}".format(obj))
        try:
            assert obj is None
        except AssertionError:
            LogTest.error(TAG, "VerifyIsNone Failed: obj = {}".format(obj))
            self._verificationErrors.append(message)

    def verify_is_not_none(self, obj, message=None):
        """
        软断言对象不为None
        :param obj: 对象
        :param message: 描述信息
        :return: None
        """
        LogTest.debug(TAG, "VerifyIsNotNone: obj = {}".format(obj))
        try:
            assert obj is not None
        except AssertionError:
            LogTest.error(TAG, "VerifyIsNotNone Failed: obj = {}".format(obj))
            self._verificationErrors.append(message)

    def verify_is_instance(self, obj, cls, message=None):
        """
        软断言对象是指定类型
        :param obj: 对象
        :param cls: 类型
        :param message: 描述信息
        :return: None
        """
        LogTest.debug(TAG, "VerifyIsInstance: obj = {}, cls = {}".format(obj, cls))
        try:
            assert isinstance(obj, cls)
        except AssertionError:
            LogTest.error(TAG, "VerifyIsInstance Failed: obj = {}, cls = {}".format(obj, cls))
            self._verificationErrors.append(message)

    def verify_not_is_instance(self, obj, cls, message=None):
        """
        软断言对象不是指定类型
        :param obj: 对象
        :param cls: 类型
        :param message: 描述信息
        :return: None
        """
        LogTest.debug(TAG, "VerifyNotIsInstance: obj = {}, cls = {}".format(obj, cls))
        try:
            assert not isinstance(obj, cls)
        except AssertionError:
            LogTest.error(TAG, "VerifyNotIsInstance Failed: obj = {}, cls = {}".format(obj, cls))
            self._verificationErrors.append(message)

    def verify_errors(self):
        """
        软断言，如果有错误，抛出异常
        :return: None
        """
        if len(self._verificationErrors) > 0:
            raise AssertionError("SoftAssert Failed, Errors appeared")
        else:
            LogTest.debug(TAG, "SoftAssert Passed")
            self._verificationErrors.clear()
