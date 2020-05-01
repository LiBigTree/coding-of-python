import requests
from bs4 import BeautifulSoup
import re


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

    soup = BeautifulSoup(demo, "html.parser")
    # 查找所有链接
    for link in soup.find_all('a'):
        print(link.get('href'))
    # .find_all(name, attrs, recursive, string, **kwargs)
    # 返回一个列表类型，储存查找的结果
    # name:对应标签名称的检索字符串
    # print(soup.find_all(['a', 'b']))
    # -True可以将显示所有标签
    # print(soup.find_all(True))
    # -显示以b开头的内容
    for tag in soup.find_all(re.compile('b')):
        print('re', tag.name)

    # attrs: 对标签属性值的检索字符串，可标注属性检索
    print('查找p标签中包含course属性的内容：{}'.format(soup.find_all('p', 'course')))
    print('指定id属性的查找：{}'.format(soup.find_all(id='link1')))

    # recursive:是否对子孙全部检索，默认True
    print(soup.find_all('a', recursive=False))

    # string: 对标签中字符串区域的检索字符串
    print(soup(string="Basic Python"))  # 简化写法
    # 单纯使用find_all搜索需要精准信息，若要实现模糊搜索，则需要正则表达式库
    print(soup.find_all(string=re.compile("python")))

    # 由于find_all函数非常常用，有如下等价：
    # <tag>(..) = <tag>.find_all(..)
    # soup(..) = soup.find_all(..)
    # find_all 有七个拓展方法
