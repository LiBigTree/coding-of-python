# 文件基础操作的练习
# ----open函数----
# 1、新文件里写入内容
with open('test.txt', 'r') as f:
    # r = f.write('hello world!')  # write方法返回写入的字符的个数
    # print(r)
    content = f.read()  # read方法返回以字符串形式文件里的内容
    print(content)

# 练习在文件里写入内容并显示当前文件内容

