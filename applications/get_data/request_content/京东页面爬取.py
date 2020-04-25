# 爬取内容：
# https://item.jd.com/100012015134.html#crumb-wrap
import requests


def jd_crawl(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        # print('1:', r.status_code)
        # print('2:', r.encoding)
        print('3:', r.text[:1000])
    except:
        print("爬取失败")


if __name__ == '__main__':
    url = "https://item.jd.com/100012015134.html"
    jd_crawl(url)
