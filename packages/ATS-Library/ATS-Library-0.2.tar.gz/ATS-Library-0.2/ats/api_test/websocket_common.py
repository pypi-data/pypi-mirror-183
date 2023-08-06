import json
import time

import websocket

TAG = "WebSocketCommon"


class WebSocketCommon(object):

    def __init__(self, host, port, path, timeout=10):
        self._host = host
        self._port = port
        self._path = path
        self._timeout = timeout
        self._ws = None

    def connect(self):
        """
        连接websocket
        :return: None
        """
        self._ws = websocket.create_connection(
                "ws://%s:%d/%s" % (self._host, self._port, self._path),
                timeout=self._timeout)

    def disconnect(self):
        """
        断开websocket连接
        :return: None
        """
        if self._ws:
            self._ws.close()
            self._ws = None

    def send(self, message):
        """
        发送消息
        :param message: 消息内容
        :return: None
        """
        if self._ws:
            self._ws.send(message)

    def recv(self):
        """
        接收消息
        :return: 消息内容
        """
        if self._ws:
            return self._ws.recv()
        return None

    def recv_all(self):
        """
        接收所有消息
        :return: 消息列表
        """
        messages = []
        while True:
            message = self.recv()
            if not message:
                break
            messages.append(message)
        return messages

    def recv_all_json(self):
        """
        接收所有消息并解析为json
        :return: 消息列表
        """
        return [json.loads(message) for message in self.recv_all()]

    def recv_all_json_with_timeout(self, timeout):
        """
        接收所有消息并解析为json，超时则返回
        :param timeout: 超时时间
        :return: 消息列表
        """
        messages = []
        start_time = time.time()
        while True:
            message = self.recv()
            if not message:
                if time.time() - start_time > timeout:
                    break
                time.sleep(0.1)
                continue
            messages.append(json.loads(message))
        return messages
