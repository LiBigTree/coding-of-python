#!/usr/bin/env python
# -*- coding:utf-8 -*-
# datetime:2020/3/21 10:51

import requests
from bs4 import BeautifulSoup
import re

# ----数据获取与解析----
# 获取
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                         ' AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/80.0.3987.149 Safari/537.36'}
r = requests.get('https://book.douban.com/subject/25986341/comments/',
                 headers=headers)

soup = BeautifulSoup(r.text, 'lxml')
pattern = soup.find_all('span', 'short')
# print(pattern)
for item in pattern:
    print(item.string)


# 正则表达式获取评星
# pattern_s = re.compile('<span class="user-stars allstar(.*?) rating')
# # print(type(pattern_s))
# p = re.findall(pattern_s, r.text)
# print(p)
# # 计算评星总和
# s = 0
# for star in p:
#     s += int(star)
# print(s)
