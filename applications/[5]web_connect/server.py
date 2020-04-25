#!/usr/bin/env python
# -*- coding:utf-8 -*-
# datetime:2020/2/17 19:13

import socket           # 导入socket库
import time    # 导入time库


HOST = '192.168.43.28'        # 连接本地服务器
PORT = 8001               # 设置端口号
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       # 选择IPv4地址以及TCP协议
sock.bind((HOST, PORT))          # 绑定端口
sock.listen(5)                   # 监听这个端口，可连接最多5个设备
while True:
    connection, address = sock.accept()              # 接受客户端的连接请求
    try:
        connection.settimeout(10)                      # 设置10s时限
        buf = connection.recv(1024)                    # 接收数据实例化
        if buf:                                 # 接收成功
            print('connection success!')
            connection.send(b'welcome to server!')        # 发送消息，b为bytes类型
        else:                                   # 接收失败
            connection.send(b'please go out!')
    except socket.timeout:                      # 超时
        print('time out')
    connection.close()    # 关闭连接
