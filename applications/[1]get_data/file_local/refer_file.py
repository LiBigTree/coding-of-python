# # 01、打开文件
# # open(file, mode='r', buffering=-1, encoding_=None, errors=None, newline=None, closefd=True, opener=None)
# # 使用open函数来打开一个文件
# # 参数：
# #   file 要打开的文件的名字（路径）
# # 返回值：
# #   返回一个对象，这个对象就代表了当前打开的文件
#
# # 创建一个变量，来保存文件的名字
# # 如果目标文件和当前文件在同一级目录下，则直接使用文件名即可
# file_name = 'demo.txt'
#
# # 在windows系统使用路径时，可以使用/来代替 \
# # 或者可以使用 \\ 来代替 \
# # 或者也可以使用原始字符串
# file_name = 'hello\\demo.txt'
# file_name = r'hello\demo.txt'
#
# # 表示路径，可以使用..来返回一级目录
# file_name = '../hello/demo.txt'
#
# # 如果目标文件距离当前文件比较远，此时可以使用绝对路径
# # 绝对路径应该从磁盘的根目录开始书写
# file_name = r'C:\Users\lilichao\Desktop\hello.txt'
#
# # file_obj = open(file_name) # 打开 file_name 对应的文件
#
# # print(file_obj)
#
#
# # 2、关闭文件
# # 打开文件
# file_name = 'demo.txt'
#
# # 调用open()来打开文件
# # file_obj = open(file_name)
#
# # # 当我们获取了文件对象以后，所有的对文件的操作都应该通过对象来进行
# # # 读取文件中的内容
# # # read()方法，用来读取文件中的内容，它会将内容全部保存为一个字符串返回
# # content = file_obj.read()
#
# # print(content)
#
# # # 关闭文件
# # # 调用close()方法来关闭文件
# # file_obj.close()
#
# # with ... as 语句
# # with open(file_name) as file_obj :
# #     # 在with语句中可以直接使用file_obj来做文件操作
# #     # 此时这个文件只能在with中使用，一旦with结束则文件会自动close()
# #     print(file_obj.read())
#
#
# file_name = 'hello'
#
# try:
#     with open(file_name) as file_obj :
#         print(file_obj.read())
# except FileNotFoundError:
#     print(f'{file_name} 文件不存在~~')
#
# # 3、文件的读取
#
# file_name = 'demo2.txt'
#
# try:
#     # 调用open()来打开一个文件，可以将文件分成两种类型
#     # 一种，是纯文本文件（使用utf-8等编码编写的文本文件）
#     # 一种，是二进制文件（图片、mp3、ppt等这些文件）
#     # open()打开文件时，默认是以文本文件的形式打开的，但是open()默认的编码为None
#     #   所以处理文本文件时，必须要指定文件的编码
#     with open(file_name,encoding='utf-8') as file_obj:
#         # 通过 read() 来读取文件中的内容
#         # 如果直接调用read()它会将文本文件的所有内容全部都读取出来
#         #   如果要读取的文件较大的话，会一次性将文件的内容加载到内存中，容易导致内存泄漏
#         #   所以对于较大的文件，不要直接调用read()
#         # help(file_obj.read)
#         # read()可以接收一个size作为参数，该参数用来指定要读取的字符的数量
#         #   默认值为-1，它会读取文件中的所有字符
#         #   可以为size指定一个值，这样read()会读取指定数量的字符，
#         #       每一次读取都是从上次读取到位置开始读取的
#         #       如果字符的数量小于size，则会读取剩余所有的
#         #       如果已经读取到了文件的最后了，则会返回''空串
#         # content = file_obj.read(-1)
#         content = file_obj.read(6)
#         content = file_obj.read(6)
#         content = file_obj.read(6)
#         content = file_obj.read(6)
#         # print(content)
#         # print(len(content))
# except FileNotFoundError :
#     print(f'{file_name} 这个文件不存在！')
#
# # 读取大文件的方式
# file_name = 'demo.txt'
#
# try:
#     with open(file_name,encoding='utf-8') as file_obj:
#         # 定义一个变量，来保存文件的内容
#         file_content = ''
#         # 定义一个变量，来指定每次读取的大小
#         chunk = 100
#         # 创建一个循环来读取文件内容
#         while True:
#             # 读取chunk大小的内容
#             content = file_obj.read(chunk)
#
#             # 检查是否读取到了内容
#             if not content:
#                 # 内容读取完毕，退出循环
#                 break
#
#             # 输出内容
#             # print(content,end='')
#             file_content += content
#
# except FileNotFoundError:
#     print(f'{file_name} 这个文件不存在！')
#
#
# print(file_content)
#
#
# # 4、文件读取2
# import pprint
# import os
#
# file_name = 'demo.txt'
#
# with open(file_name, encoding='utf-8') as file_obj:
#     # readline()
#     # 该方法可以用来读取一行内容
#     # print(file_obj.readline(),end='')
#     # print(file_obj.readline())
#     # print(file_obj.readline())
#
#     # readlines()
#     # 该方法用于一行一行的读取内容，它会一次性将读取到的内容封装到一个列表中返回
#     # r = file_obj.readlines()
#     # pprint.pprint(r[0])
#     # pprint.pprint(r[1])
#     # pprint.pprint(r[2])
#
#     for t in file_obj:
#         print(t)
#
# # 5、文件的写入
# file_name = 'demo5.txt'
#
# # 使用open()打开文件时必须要指定打开文件所要做的操作（读、写、追加）
# # 如果不指定操作类型，则默认是 读取文件 ， 而读取文件时是不能向文件中写入的
# # r 表示只读的
# # w 表示是可写的，使用w来写入文件时，如果文件不存在会创建文件，如果文件存在则会截断文件
# #   截断文件指删除原来文件中的所有内容
# # a 表示追加内容，如果文件不存在会创建文件，如果文件存在则会向文件中追加内容
# # x 用来新建文件，如果文件不存在则创建，存在则报错
# # + 为操作符增加功能
# #   r+ 即可读又可写，文件不存在会报错
# #   w+
# #   a+
# with open(file_name , 'w' , encoding='utf-8') as file_obj:
#     # with open(file_name , 'r+' , encoding='utf-8') as file_obj:
#     # with open(file_name, 'x', encoding='utf-8') as file_obj:
#     # write()来向文件中写入内容，
#     # 如果操作的是一个文本文件的话，则write()需要传递一个字符串作为参数
#     # 该方法会可以分多次向文件中写入内容
#     # 写入完成以后，该方法会返回写入的字符的个数
#     file_obj.write('aaa\n')
#     file_obj.write('bbb\n')
#     file_obj.write('ccc\n')
#     r = file_obj.write(str(123)+'123123\n')
#     r = file_obj.write('今天天气真不错')
#     print(r)
#
# # 6、文件
# # file_name = 'c:/Users/.../告白气球.flac'
#
# # 读取模式
# # t 读取文本文件（默认值）
# # b 读取二进制文件
#
# with open(file_name, 'rb') as file_obj:
#     # 读取文本文件时，size是以字符为单位的
#     # 读取二进制文件时，size是以字节为单位
#     # print(file_obj.read(100))
#
#     # 将读取到的内容写出来
#     # 定义一个新的文件
#     new_name = 'aa.flac'
#
#     with open(new_name , 'wb') as new_obj:
#
#         # 定义每次读取的大小
#         chunk = 1024 * 100
#
#         while True :
#             # 从已有的对象中读取数据
#             content = file_obj.read(chunk)
#
#             # 内容读取完毕，终止循环
#             if not content :
#                 break
#
#             # 将读取到的数据写入到新对象中
#             new_obj.write(content)
#
#
# # 7、读取文件的位置
# # with open('demo.txt','rb') as file_obj:
# #     # print(file_obj.read(100))
# #     # print(file_obj.read(30))
#
# #     # seek() 可以修改当前读取的位置
# #     file_obj.seek(55)
# #     file_obj.seek(80,0)
# #     file_obj.seek(70,1)
# #     file_obj.seek(-10,2)
# #     # seek()需要两个参数
# #     #   第一个 是要切换到的位置
# #     #   第二个 计算位置方式
# #     #       可选值：
# #     #           0 从头计算，默认值
# #     #           1 从当前位置计算
# #     #           2 从最后位置开始计算
#
# #     print(file_obj.read())
#
# #     # tell() 方法用来查看当前读取的位置
# #     print('当前读取到了 -->',file_obj.tell())
#
# with open('demo2.txt','rt' , encoding='utf-8') as file_obj:
#     # print(file_obj.read(100))
#     # print(file_obj.read(30))
#
#     # seek() 可以修改当前读取的位置
#     file_obj.seek(9)
#     # seek()需要两个参数
#     #   第一个 是要切换到的位置
#     #   第二个 计算位置方式
#     #       可选值：
#     #           0 从头计算，默认值
#     #           1 从当前位置计算
#     #           2 从最后位置开始计算
#
#     print(file_obj.read())
#
#     # tell() 方法用来查看当前读取的位置
#     print('当前读取到了 -->',file_obj.tell())
#
# # 8、文件的其他操作
#
# import os
# from pprint import pprint
#
# # os.listdir() 获取指定目录的目录结构
# # 需要一个路径作为参数，会获取到该路径下的目录结构，默认路径为 . 当前目录
# # 该方法会返回一个列表，目录中的每一个文件（夹）的名字都是列表中的一个元素
# r = os.listdir()
#
# # os.getcwd() 获取当前所在的目录
# r = os.getcwd()
#
# # os.chdir() 切换当前所在的目录 作用相当于 cd
# # os.chdir('c:/')
#
# # r = os.getcwd()
#
# # 创建目录
# # os.mkdir("aaa") # 在当前目录下创建一个名字为 aaa 的目录
#
# # 删除目录
# # os.rmdir('abc')
#
# # open('aa.txt','w')
# # 删除文件
# # os.remove('aa.txt')
#
# # os.rename('旧名字','新名字') 可以对一个文件进行重命名，也可以用来移动一个文件
# # os.rename('aa.txt','bb.txt')
# os.rename('bb.txt','c:/users/lilichao/desktop/bb.txt')
#
# pprint(r)
