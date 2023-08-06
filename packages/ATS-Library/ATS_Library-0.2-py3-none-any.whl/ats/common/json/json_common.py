import json


class JsonCommon(object):

    def __init__(self, json_file):
        self.json_file = json_file
        self.json_data = self.read_json_file()

    def read_json_file(self):
        """
        读取json文件
        :return: json数据
        """
        with open(self.json_file, 'r') as f:
            return json.load(f)

    def get_json_data(self):
        """
        获取json数据
        :return: json数据
        """
        return self.json_data

    def get_json_data_by_key(self, key):
        """
        根据key获取json数据
        :param key: key
        :return: json数据
        """
        return self.json_data[key]

    def get_json_data_by_key_and_index(self, key, index):
        """
        根据key和索引获取json数据
        :param key: key
        :param index: 索引
        :return: json数据
        """
        return self.json_data[key][index]
