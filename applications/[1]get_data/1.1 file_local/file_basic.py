# -*- coding: UTF-8 -*-
# 文件基础操作的练习
# ----open函数----
# open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)
# help(open)可以查看用法或者直接在pycharm中查看
# file：文件路径；mode：文件打开模式，默认为r；buffering：缓冲，默认-1，0代表不缓冲
# 返回文件对象
# with open('test.txt', 'r', encoding='UTF-8') as f:
#     # r = f.write('hello world!')  # write方法返回写入的字符的个数
#     # print(r)
#     content = f.read()  # read方法返回以字符串形式文件里的内容
#     print(content)

# 关闭和读写文件相关的函数和方法
# # 写入内容
# with open(r'test2.txt', 'w+', encoding='UTF-8') as f:
#     f.write("测试成功！")
#
# # 读取内容
# with open(r'test2.txt', encoding='UTF-8') as f:
#     p1 = f.read(2)
#     p2 = f.read()  # 不带参数会直接读完
# print(p1, p2)

# f.readlines()/writelines() 读取或写入多行内容
# 返回列表，且有换行符存在 > 可以用strip方法去掉
# con2 = []
# with open('test.txt', 'r', encoding='UTF-8') as f:
#     con = f.readlines()
#     for i in range(len(con)-1):
#         con2.append(con[i].strip('\n'))
#
# print(con2)

# 将test文件编号写入新文件
with open('test.txt', 'r', encoding='UTF-8') as f:
    con = f.readlines()
    for i in range(len(con)):
        con[i] = str(i+1) + ' ' + con[i]
    with open('order.txt', 'w', encoding='UTF-8') as f2:
        f2.writelines(con)

# 文件尾部加上一行字符串
with open('test.txt', 'a+', encoding='UTF-8') as f3:
    f3.writelines('\n')
    f3.writelines('等容光焕新 如世间新生')
    con_add = f3.readlines()
    print(con_add)
