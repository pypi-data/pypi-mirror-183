import csv


class CsvCommon(object):

    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.csv_data = self.read_csv()

    def read_csv(self):
        """
        读取csv文件
        :return: csv文件数据
        """
        with open(self.csv_file, "r") as f:
            reader = csv.reader(f)
            return [row for row in reader]

    def get_csv_data(self):
        """
        获取csv文件数据
        :return: csv文件数据
        """
        return self.csv_data

    def get_csv_data_by_row(self, row):
        """
        获取csv文件指定行数据
        :param row: 行数
        :return: 指定行数据
        """
        return self.csv_data[row]

    def get_csv_data_by_column(self, column):
        """
        获取csv文件指定列数据
        :param column: 列数
        :return: 指定列数据
        """
        return [row[column] for row in self.csv_data]

    def get_csv_data_by_row_column(self, row, column):
        """
        获取csv文件指定行列数据
        :param row: 行数
        :param column: 列数
        :return: 指定行列数据
        """
        return self.csv_data[row][column]
