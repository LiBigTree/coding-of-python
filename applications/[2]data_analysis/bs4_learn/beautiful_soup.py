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
    # ----内容解析 五种基本元素：----
    soup = BeautifulSoup(demo, "html.parser")
    # print([n for n in dir(soup) if not n.startswith('_')])  # 查看返回对象内容
    # print('页面的标题:', soup.title)
    #
    # print('获取a标签的内容:', soup.a)  # 如果有两个以上，获取第一个
    # print('标签的类型：{}'.format(type(soup.a)))
    # print('获取a标签的名字:', soup.a.name)
    # print('a的父亲的名字: {}'.format(soup.a.parent.name))
    #
    # print('标签的属性: {}'.format(soup.a.attrs))  # 属性返回的是字典，可以进行字典相关的操作
    # {'href': 'http://www.icourse163.org/course/BIT-268001', 'class': ['py1'], 'id': 'link1'}
    # href: hypertext reference 超文本链接

    print('非属性字符串是字符串的形式：{}'.format(soup.a.string))

    # 注释 <!--comment-->
    comment = "<b><!--this is a comment--></b><p>this is not a comment</p>"
    soup2 = BeautifulSoup(comment, "html.parser")
    print("注释的类型是：", type(soup2.b.string))
    print("属性的类型是：", type(soup2.p.string))
