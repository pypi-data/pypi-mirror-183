import requests


class HttpCommon(object):

    def __init__(self, url, method, data=None, headers=None, cookies=None, files=None, timeout=10):
        self.url = url
        self.method = method
        self.data = data
        self.headers = headers
        self.cookies = cookies
        self.files = files
        self.timeout = timeout

    def send_request(self):
        """
        发送请求
        :return: 响应
        """
        if self.method == "get":
            response = requests.get(url=self.url, params=self.data, headers=self.headers, cookies=self.cookies,
                                    timeout=self.timeout)
        elif self.method == "post":
            response = requests.post(url=self.url, data=self.data, headers=self.headers, cookies=self.cookies,
                                     files=self.files, timeout=self.timeout)
        elif self.method == "put":
            response = requests.put(url=self.url, data=self.data, headers=self.headers, cookies=self.cookies,
                                    timeout=self.timeout)
        elif self.method == "delete":
            response = requests.delete(url=self.url, data=self.data, headers=self.headers, cookies=self.cookies,
                                       timeout=self.timeout)
        else:
            response = None
        return response

    def get_response(self):
        """
        获取响应
        :return: 响应
        """
        response = self.send_request()
        return response

    def get_response_json(self):
        """
        获取响应json
        :return: 响应json
        """
        response = self.send_request()
        return response.json()

    def get_response_text(self):
        """
        获取响应文本
        :return: 响应文本
        """
        response = self.send_request()
        return response.text

    def get_response_status_code(self):
        """
        获取响应状态码
        :return: 响应状态码
        """
        response = self.send_request()
        return response.status_code

    def get_response_headers(self):
        """
        获取响应头
        :return: 响应头
        """
        response = self.send_request()
        return response.headers

    def get_response_cookies(self):
        """
        获取响应cookies
        :return: 响应cookies
        """
        response = self.send_request()
        return response.cookies

    def get_response_content(self):
        """
        获取响应内容
        :return: 响应内容
        """
        response = self.send_request()
        return response.content

    def get_response_encoding(self):
        """
        获取响应编码
        :return: 响应编码
        """
        response = self.send_request()
        return response.encoding

    def get_response_reason(self):
        """
        获取响应原因
        :return: 响应原因
        """
        response = self.send_request()
        return response.reason

    def get_response_is_redirect(self):
        """
        获取响应是否重定向
        :return: 响应是否重定向
        """
        response = self.send_request()
        return response.is_redirect

    def verify_response_is_permanent_redirect(self):
        """
        验证响应是否永久重定向
        :return: 响应是否永久重定向
        """
        response = self.send_request()
        return response.is_permanent_redirect

    def verify_response_is_ok(self):
        """
        验证响应是否成功
        :return: 响应是否成功
        """
        response = self.send_request()
        return response.ok

    def get_response_history(self):
        """
        获取响应历史
        :return: 响应历史
        """
        response = self.send_request()
        return response.history

    def get_response_links(self):
        """
        获取响应链接
        :return: 响应链接
        """
        response = self.send_request()
        return response.links

    def get_response_next(self):
        """
        获取响应下一个
        :return: 响应下一个
        """
        response = self.send_request()
        return response.next

    def get_response_url(self):
        """
        获取响应url
        :return: 响应url
        """
        response = self.send_request()
        return response.url

    def get_response_elapsed(self):
        """
        获取响应时间
        :return: 响应时间
        """
        response = self.send_request()
        return response.elapsed

    def get_response_raw(self):
        """
        获取响应原始
        :return: 响应原始
        """
        response = self.send_request()
        return response.raw

    def get_response_request(self):
        """
        获取响应请求
        :return: 响应请求
        """
        response = self.send_request()
        return response.request

    def get_response_apparent_encoding(self):
        """
        获取响应编码
        :return: 响应编码
        """
        response = self.send_request()
        return response.apparent_encoding

    def get_response_close(self):
        """
        获取响应关闭
        :return: 响应关闭
        """
        response = self.send_request()
        return response.close
