# http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html
import requests
from bs4 import BeautifulSoup
import bs4


def crawl_data(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        # print('1:', r.status_code)
        # print('2:', r.encoding)
        return r.text
    except:
        return ''


def get_data(u_list, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            u_list.append([tds[0].string, tds[1].string, tds[2].string])


def output_data(u_list, num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}\t"  # {3}啥意思呢
    print(tplt.format("排名", "学校名称", "总分", chr(12288)))  # 12288 表示中文字符的空格
    for i in range(num):
        u = u_list[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))
    # print(u_list)


if __name__ == '__main__':
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html"
    u_info = []
    html = crawl_data(url)
    get_data(u_info, html)
    output_data(u_info, 20)
