# 百度关键字接口：http://www.baidu.com/s?wd=keyword
from applications.config import config
import requests

try:
    url = 'http://www.baidu.com/s'  # 这里不是https 为啥呢
    hd = {
        "User-Agent": config.ConfigCrawl.user,
        "cookie": config.ConfigCrawl.cok
    }
    kw = {"wd": "Python"}

    r = requests.get(url, headers=hd, params=kw)

    print(r.status_code)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    # print(r.text)
    print(len(r.text))
except:
    print("爬取异常")


