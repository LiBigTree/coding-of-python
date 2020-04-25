#!/usr/bin/env python
# -*- coding:utf-8 -*-
# datetime:2020/3/20 20:36

import requests
from parsel import Selector


# ----弹幕数据获取与解析----
# 获取
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                         ' AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/80.0.3987.149 Safari/537.36'}
r = requests.get('https://api.bilibili.com/x/v1/dm/list.so?oid=2238927',
                 headers=headers, timeout=30).content

# 用scrapy出品的parsel
# 乱码问题
xbody = Selector(text=str(r, encoding='utf-8'))
lists = xbody.xpath("//d")
count = xbody.xpath("//maxlimit/text()").extract_first()
print("共有%s条弹幕" % count)
for li in lists:
    content = li.xpath("./text()").extract_first()
    par = li.xpath("./@p").extract_first()
    print(content, ":::::", par)

