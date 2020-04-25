import requests

# ----requests库----
# 一、request 的七个方法:
# 1、requests.request(method, url, **kwargs) 本质上是一个request方法，出于实际处理，细分到7种方法
# method: GET、HEAD、POST、PUT、PATCH、DELETE、(OPTIONS)

# **kwargs: 控制访问的参数，可选
# 第一个：params： 字典或字典序列，作为参数增加到url中
kv = {'key1': 'value1', 'key2': 'value2'}
r = requests.request('GET', 'http://python123.io/ws', params=kv)
print("1.1: ", r.url)
# 第二个：data，字典、字节序列或文件对象，作为request的内容
# 第三个：json，JSON格式的数据，作为Request的内容
# 第四个：headers，字典，HTTP定制头 模拟浏览器实现用户访问

# 第五个：cookies，字典或CookieJar，request中的cookie
# 第六个：auth，元组，支持HTTP认证功能
# 第七个：files，字典类型，传输文件，向某一链接提交某一文件，和open搭配使用
# fs = {'file': open('data.txt', 'rb')}
# r = requests.request('POST', 'http://python123.io/ws', files=fs)
# 第八个：timeout，设定超时时间，秒为单位
# r = requests.request('GET', 'http://www.baidu.com', timeout=10)
# 第九个：proxies，字典类型，设定访问代理服务器，可以增加登录认证， 有效防止爬虫逆追踪

# 第十个：allow_redirects:True/False, 默认为True，重定向开关
# 第十一个：stream，True/False, 默认为True，获取内容立即下载开关
# 第十二个：verify，True/False, 默认为True，认证SSL证书的开关
# 第十三个：cert，本地SSL证书路径

# 细分：
# 2、.get 获取网页的主要方法，对应HTTP的GET
# 构造一个服务器请求资源的request对象
# 返回一个包含服务器资源的Response对象
# （url， params>(额外参数字典或者字节流格式，可选)， **kwargs>(12个控制访问的参数)）

# r = requests.get("http://www.baidu.com")
# print(r.headers)
# print(type(r))

# 这些方法独立出来的原因是 针对性操作可以节省网络资源，只获取需要的内容
# 3、.head() 网页头信息，对应HEAD
# r = requests.head("http://www.baidu.com")
# print("3.1: ", r.headers)
# print("3.2: ", r.text)

# 4、.post() 提交POST请求 附加新的数据
# 提交表单或者数据
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.post('http://httpbin.org/post', data='ABC')
# print("4.1: ", r.text)
# r = requests.post('http://httpbin.org/post', data=payload)
# # httpbin是一个HTTP Request & Response Service，你可以向他发送请求，然后他会按照指定的规则将你的请求返回
# # 用来进行请求调试的学习
# print("4.2: ", r.text)
# 两次操作互相独立

# 5、.put() 提交PUT请求 存储一个资源，覆盖原URL位置的资源
# 6、.patch() 提交网页局部修改请求
# 7、.delete 提交删除请求

# ----属性----

# # 二、response对象的五个重要属性
# # 1）检测请求的状态码 200表示正常 404表示连接失败
# print("1: ", r.status_code)
# # 2）HTTP相应内容的字符串形式>url对应的页面内容
# print("2: ", r.text)
# # 3) 从HTTP header中猜测的响应内容编码方式
# print("3: ", r.encoding)
# # 4）从内容中分析出的响应内容编码方式（备选编码方式）
# print("4: ", r.apparent_encoding)
# # 5) HTTP响应内容的二进制形式
# print("5: ", r.content)


# 备注：4和5 区别：4从header中的charset获取编码方式，
# 如果不存在，则认为是ISO-8859-1
# 5根据网页内容解析，更准确一些


# 三、 ----通--用--代--码--框--架----
# 考虑请求异常时处理方法
# requests.(1ConnectionError:
# /2 HTTPError HTTP错误异常
# /3 URLRequired URL缺失异常
# /4 TooManyRedirects 超过最大重定向次数，产生重定向异常：指对复杂链接
# /5 ConnectTimeout 连接远程服务器超时异常
# /6 请求URL超时，产生超时异常)

# 异常判断函数：判断返回状态不是200，显示产生异常

# def getHTMLText(url):
#     try:
#         r = requests.get(url, timeout=30)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#         return "有异常了"
#
#
# if __name__ == '__main__':
#     url = "http://github.com/"
#     print(getHTMLText(url))
