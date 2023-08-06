from ats.common.log.log import LogTest

TAG = "Assertion"


class Assertion(object):

    @staticmethod
    def assert_equal(actual, expected, message=None):
        """
        断言相等
        :param actual: 实际值
        :param expected: 期望值
        :param message: 描述信息
        :return: None
        """
        LogTest.debug(TAG, "AssertEquals: actual = {}, expected = {}".format(actual, expected))
        if actual == expected:
            return
        LogTest.error(TAG, "AssertEquals Failed: actual = {}, expected = {}".format(actual, expected))
        raise AssertionError(message)

    @staticmethod
    def assert_not_equal(actual, expected, message=None):
        """
        断言不相等
        :param actual: 实际值
        :param expected: 期望值
        :param message: 描述信息
        :return: None
        """
        LogTest.debug(TAG, "AssertNotEquals: actual = {}, expected = {}".format(actual, expected))
        if actual != expected:
            return
        LogTest.error(TAG, "AssertNotEquals Failed: actual = {}, expected = {}".format(actual, expected))
        raise AssertionError(message)

    @staticmethod
    def assert_true(condition, message=None):
        """
        断言条件为真
        :param condition: 条件
        :param message: 描述信息
        :return: None
        """
        LogTest.debug(TAG, "AssertTrue: condition = {}".format(condition))
        if condition:
            return
        LogTest.error(TAG, "AssertTrue Failed: condition = {}".format(condition))
        raise AssertionError(message)

    @staticmethod
    def assert_false(condition, message=None):
        """
        断言条件为假
        :param condition: 条件
        :param message: 描述信息
        :return: None
        """
        LogTest.debug(TAG, "AssertFalse: condition = {}".format(condition))
        if not condition:
            return
        LogTest.error(TAG, "AssertFalse Failed: condition = {}".format(condition))
        raise AssertionError(message)

    @staticmethod
    def assert_in(member, container, message=None):
        """
        断言成员在容器中
        :param member: 成员
        :param container: 容器
        :param message: 描述信息
        :return: None
        """
        LogTest.debug(TAG, "AssertIn: member = {}, container = {}".format(member, container))
        if member in container:
            return
        LogTest.error(TAG, "AssertIn Failed: member = {}, container = {}".format(member, container))
        raise AssertionError(message)

    @staticmethod
    def assert_not_in(member, container, message=None):
        """
        断言成员不在容器中
        :param member: 成员
        :param container: 容器
        :param message: 描述信息
        :return: None
        """
        LogTest.debug(TAG, "AssertNotIn: member = {}, container = {}".format(member, container))
        if member not in container:
            return
        LogTest.error(TAG, "AssertNotIn Failed: member = {}, container = {}".format(member, container))
        raise AssertionError(message)

    @staticmethod
    def assert_is(var1, var2, message=None):
        """
        断言两个变量是同一个对象
        :param var1: 变量1
        :param var2: 变量2
        :param message: 描述信息
        :return: None
        """
        LogTest.debug(TAG, "AssertIs: var1 = {}, var2 = {}".format(var1, var2))
        if var1 is var2:
            return
        LogTest.error(TAG, "AssertIs Failed: var1 = {}, var2 = {}".format(var1, var2))
        raise AssertionError(message)

    @staticmethod
    def assert_is_not(var1, var2, message=None):
        """
        断言两个变量不是同一个对象
        :param var1: 变量1
        :param var2: 变量2
        :param message: 描述信息
        :return: None
        """
        LogTest.debug(TAG, "AssertIsNot: var1 = {}, var2 = {}".format(var1, var2))
        if var1 is not var2:
            return
        LogTest.error(TAG, "AssertIsNot Failed: var1 = {}, var2 = {}".format(var1, var2))
        raise AssertionError(message)

    @staticmethod
    def assert_is_none(var, message=None):
        """
        断言变量为空
        :param var: 变量
        :param message: 描述信息
        :return: None
        """
        LogTest.debug(TAG, "AssertNone: var = {}".format(var))
        if var is None:
            return
        LogTest.error(TAG, "AssertNone Failed: var = {}".format(var))
        raise AssertionError(message)

    @staticmethod
    def assert_is_not_none(var, message=None):
        """
        断言变量不为空
        :param var: 变量
        :param message: 描述信息
        :return: None
        """
        LogTest.debug(TAG, "AssertNotNone: var = {}".format(var))
        if var is not None:
            return
        LogTest.error(TAG, "AssertNotNone Failed: var = {}".format(var))
        raise AssertionError(message)

    @staticmethod
    def assert_is_instance(obj, cls, message=None):
        """
        断言对象是指定类型
        :param obj: 对象
        :param cls: 类型
        :param message: 描述信息
        :return: None
        """
        LogTest.debug(TAG, "AssertIsInstance: obj = {}, cls = {}".format(obj, cls))
        if isinstance(obj, cls):
            return
        LogTest.error(TAG, "AssertIsInstance Failed: obj = {}, cls = {}".format(obj, cls))
        raise AssertionError(message)

    @staticmethod
    def assert_not_is_instance(obj, cls, message=None):
        """
        断言对象不是指定类型
        :param obj: 对象
        :param cls: 类型
        :param message: 描述信息
        :return: None
        """
        LogTest.debug(TAG, "AssertNotIsInstance: obj = {}, cls = {}".format(obj, cls))
        if not isinstance(obj, cls):
            return
        LogTest.error(TAG, "AssertNotIsInstance Failed: obj = {}, cls = {}".format(obj, cls))
        raise AssertionError(message)
