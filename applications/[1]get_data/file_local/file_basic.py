# 文件基础操作的练习
# ----open函数----
# open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)
# help(open)可以查看用法或者直接在pycharm中查看
# file：文件路径；mode：文件打开模式，默认为r；buffering：缓冲，默认-1，0代表不缓冲
# 返回文件对象
with open('test.txt', 'r') as f:
    # r = f.write('hello world!')  # write方法返回写入的字符的个数
    # print(r)
    content = f.read()  # read方法返回以字符串形式文件里的内容
    print(content)




