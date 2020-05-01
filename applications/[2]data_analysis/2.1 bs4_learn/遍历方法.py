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
    # ---- 上行遍历 ----
    soup = BeautifulSoup(demo, "html.parser")

    # print(soup.head)
    # print(soup.head.contents)  # head标签的儿子，被放入一个列表了

    # print(soup.body.contents)  # 标签不仅仅包括儿子节点，还包括格式字符串之类的信息
    # # 获取儿子节点数量
    # print('body儿子节点数量:', len(soup.body.contents))
    # print('检索第一个：', soup.body.contents[1])
    #
    # # 遍历儿子节点
    # for child in soup.body.children:
    #     print(child)

    # 遍历子孙节点, 存在子孙节点才能遍历成功
    # for child in soup.body.descendents:
    #     print(child)

    # # ----下行遍历----
    # print(soup.title.parent)
    # print(soup.html.parent)  # html的父亲是它自己
    # print(soup.parent)  # soup没有，空的
    #
    # # 遍历时会遍历到soup本身，而它是空的，所以需要判断特殊处理
    # for parent in soup.a.parents:
    #     if parent is None:
    #         print(parent)
    #     else:
    #         print(parent.name)

    # ----平行遍历----
    print(soup.a.next_sibling)
    print(soup.a.previous_sibling)

    # 遍历后续节点
    for sibling in soup.a.next_siblings:
        print(sibling)
    # 遍历前续节点
    for sibling in soup.a.previous_sibling:
        print(sibling)
