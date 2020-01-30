# 写在字符串之前的话
# 数、字符等数据元素 >> 元组、列表、字符串等数据结构 >> 循环、选择语句 >> 模块
# 在我看来， 每一种编程语言对应的是其解决问题的思维。或者说，分解问题的思维。
# so，一学基础；二悟思想。

# 字符串基本操作 2020/1/28

# 1、 字符串转义
print(1)
print("let's go!")
print('let\'s go!')

# 2、字符串拼接
print(2)
x = "hello, "
y = "world!"
print(x+y)

# 3、字符串表示 str 和 repr
# 直接打印字符串和print显示不一样， 所以才有上述两种说法
print(3)
print(repr("hello,\nworld!"))
print(str("hello, \nworld!"))
# >> str 会转换，显示的是用户接受的； repr显示字符串

# 4、 转义字符
print(4)
print(r'C:\nowhere')
# 以反斜杠结尾的字符串另作处理，如下：
print(r'C:\Program Files''\\')

# 5、 长字符串： 三个单引号 ‘\’ 用来连接行和行
print(5)
print('''hello, \
world!''')

# url = input('please enter the url:')
#
# # https://www.github.com
# domain = url[12:-4]
#
# print("Domain name :" + domain)



