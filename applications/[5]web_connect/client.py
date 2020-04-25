#!/usr/bin/env python
# -*- coding:utf-8 -*-
# datetime:2020/2/17 19:16

import socket
import time

HOST = 'localhost'
PORT = 8001
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
time.sleep(2)
sock.send(b'1')    # 发送信息
print(sock.recv(1024).decode())     # 打印接收消息，并且译码
sock.close()     # 关闭连接
