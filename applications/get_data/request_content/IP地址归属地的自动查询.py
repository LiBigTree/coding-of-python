# www.ip138.com IP查询
# 接口：https://m.ip138.com/iplookup.asp?ip=ipaddress
import requests
from applications.config.config import ConfigCrawl


text = ''  # 输入需要查询的IP地址
hd = {
    'User-Agent': ConfigCrawl.user
}
url = "https://m.ip138.com/iplookup.asp?ip={}".format(text)
r = requests.get(url, headers=hd)
r.encoding = r.apparent_encoding
print(len(r.text))
print(r.text)
