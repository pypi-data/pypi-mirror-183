class EFormat(object):

    @staticmethod
    def element(loc, *args):
        """
        获取元素
        :param loc: 元素定位
        :param args: 元素定位参数
        :return: 元素
        """
        by, loc = loc
        return by, loc.format(*args)
