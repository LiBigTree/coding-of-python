# 网络图片链接的格式
# http://www.example.com/picture.jpg
import requests
import os


url = "http://image.ngchina.com.cn/2020/0417/20200417065115466.jpg"
root = r"D:/Daily/img/crawl/"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        # print([n for n in dir(r) if not n.startswith('_')]) # 查看返回对象内容
        print(r.status_code)
        # 保存图片
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
    else:
        print("文件已经存在")
except:
    print("爬取失败")
