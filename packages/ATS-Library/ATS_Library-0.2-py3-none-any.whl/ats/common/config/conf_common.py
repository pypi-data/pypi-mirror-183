import configparser

TAG = "ConfCommon"


class ConfCommon(object):

    def __init__(self, conf_file):
        """
        初始化配置文件
        :param conf_file: 配置文件路径
        """
        self.conf_file = conf_file
        self.conf = configparser.ConfigParser()
        self.conf.optionxform = lambda option: option
        self.conf.read(self.conf_file, encoding="utf-8")

    def get_conf(self, section, option):
        """
        获取配置文件中的值
        :param section: section名称
        :param option: option名称
        :return: option对应的值
        """
        try:
            return self.conf.get(section, option)
        except configparser.NoSectionError:
            return None
        except configparser.NoOptionError:
            return None

    def set_conf(self, section, option, value):
        """
        设置配置文件中的值
        :param section: section名称
        :param option: option名称
        :param value: option对应的值
        :return: None
        """
        try:
            self.conf.set(section, option, value)
        except configparser.NoSectionError:
            self.conf.add_section(section)
            self.conf.set(section, option, value)

    def save_conf(self):
        """
        保存配置文件
        :return: None
        """
        self.conf.write(open(self.conf_file, mode="w", encoding="utf-8"))

    def get_sections(self):
        """
        获取配置文件中的所有section
        :return: section列表
        """
        return self.conf.sections()

    def get_options(self, section):
        """
        获取配置文件中的所有option
        :param section: section名称
        :return: option列表
        """
        return self.conf.options(section)

    def get_items(self, section):
        """
        获取配置文件中的所有items
        :param section: section名称
        :return: items列表
        """
        return self.conf.items(section)

    def get_all_dict(self):
        """
        获取配置文件中的所有内容
        :return: 配置文件中的所有内容
        """
        return dict([(section, dict(self.conf.items(section))) for section in self.conf.sections()])

    def get_section_dict(self, section):
        """
        获取配置文件中section的所有内容
        :return: 配置文件中的所有内容
        """
        return dict(self.conf.items(section))
