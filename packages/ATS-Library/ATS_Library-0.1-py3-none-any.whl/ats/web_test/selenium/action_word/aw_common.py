from ats.common.config.conf_common import ConfCommon
from ats.common.log.log import LogTest

TAG = "ActionWord"
page_objs = []
global page_obj_map
global page_method_map


def set_page_obj_map(conf_path, section):
    """
    设置页面对象映射字典
    :param conf_path: 配置文件路径
    :param section: 配置文件section名
    :return: section下键值对
    """
    global page_obj_map
    page_obj_map = ConfCommon(conf_path).get_section_dict(section)


def set_page_method_map(conf_path, section):
    """
    设置页面方法映射字典
    :param conf_path: 配置文件路径
    :param section: 配置文件section名
    :return: section下键值对
    """
    global page_method_map
    page_method_map = ConfCommon(conf_path).get_section_dict(section)


class AWCommon(object):

    @staticmethod
    def execute(driver, page: str, method: str, args: dict = None):
        """
        执行测试用例
        :param driver: 浏览器驱动
        :param page: 页面名
        :param method: 方法名
        :param args: 入参
        :return: PO方法
        """

        global page_obj_map
        global page_method_map

        def _execute(_page: str):
            if _page:
                LogTest.info(TAG, "创建新对象：{}".format(_page))
                _new_page = page_obj_map.get(page)(driver)
                page_objs.append(_new_page)
            return page_objs[-1]

        page_obj = _execute(page) if page and not page == "" else page_objs[-1]
        po_method = getattr(page_obj, page_method_map.get(method))
        return po_method(args) if args and not args == "" else po_method()
