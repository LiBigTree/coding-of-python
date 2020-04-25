# 模拟网页请求时的数据


class ConfigCrawl(object):
    # 浏览器, Mozilla/5.0 是一个标准的浏览器身份标识
    user = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/80.0.3987.163 Safari/537.36 '
    # cookies 爬取时加入的cookie信息得是自己登录后的cookie（个人隐私）
    cok = ' ',
