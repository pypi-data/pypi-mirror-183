import yaml


class YamlCommon(object):

    def __init__(self, yaml_path):
        self.yaml_path = yaml_path

    def get_yaml_dict(self):
        """
        获取yaml文件内容
        :return: yaml文件内容
        """
        with open(self.yaml_path, "r", encoding="utf-8") as f:
            yaml_dict = yaml.load(f, Loader=yaml.FullLoader)
        return yaml_dict
