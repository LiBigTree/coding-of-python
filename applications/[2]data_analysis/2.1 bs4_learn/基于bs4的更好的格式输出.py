import requests
from bs4 import BeautifulSoup


def crawl_data(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        # print('1:', r.status_code)
        # print('2:', r.encoding)
        result = r.text
        return result
    except:
        print("爬取失败")


if __name__ == '__main__':
    # 网页爬取
    url = 'http://python123.io/ws/demo.html'
    demo = crawl_data(url)
    # ---- 美化输出 ----
    soup = BeautifulSoup(demo, "html.parser")
    print(soup.prettify())  # prettify方法使用对每个标签加换行符的方法来使得文档更漂亮的输出
