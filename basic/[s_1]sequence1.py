# 前言
# 一是记编程基础知识；二思索处理问题的思维。

# 逻辑线：数、字符 >> 元组、列表、字符串 >> 控制语句
# >> 函数 >> 类 >> 模块、包

# 概览： 1、字符串常用操作
# 2、 字符串设置格式
# 3、 字符串方法

# 字符串基本操作 2020/1/28
# 1、 字符串转义

print(1)
print("let's go!")
print('let\'s go!')

# 2、字符串拼接
print(2)
x = "hello, "
y = "world!"
print(x + y)

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

# ----设--置--字--符--串--格--式-----
# 总的方针是对字符串调用方法 format

# 6、 设置格式: 用要插入字符串中的值 去代替 字符串里的用花括号括起的替换字段
# 若是最终要保留花括号， 则加两个
print('6:')
print("{{ceil n'est pas une replacement field}}".format())

# 7、格式设置的方法本质是在 {}.format（） 中的大括号和小括号之间建立一种联系，大括号到小括号去找内容，然后输出
print('7:')
fullname = ["Alfred", "Smoketoomuch"]
print("Mr {name[1]}".format(name=fullname))

import math
tmpl = "The {mod.__name__} module defines the value {mod.pi} for π"
x = tmpl.format(mod=math)
print(x)
# 这里其实就是打印了 math.__name__ 和 math.pi

# 8、基本转换——进行str repr ASCII、转化
print('8:')
print("{pi!s} {pi!r} {pi!a}".format(pi="π"))

# 9、说明转化的值的类型
print('9:')
f = "The number is {num:f}".format(num=42)
b = "The number is {num:b}".format(num=42)
e = "The number is {num:e}".format(num=42)
print(f, "\n", b, "\n", e)

# 10、指定宽度、精度、千位分隔符
print('10:')
# 宽度
print("{num:10}".format(num=3))
print("{name:10}".format(name="Bob"))

# 精度
print("Pi day is {pi:10.2f}".format(pi=3.1415))

# 放在宽度和精度说明之间的 逗号 是添加千位分隔符
x = '{:20,.2f}'.format(10**10)
print(x)

# 11、符号、对齐、0填充
print('11:')

# 左对齐 <，右对齐 >，居中 ^
print('{:$^10.2f}'.format(3.14))
# $ 是填充  ^是对齐方式 10是宽度 .2f是精度说明

# 另一个知识点 ‘#’触发转化
print("{:b}".format(42))

# ----------字--符--串--方--法-----------

# 12、center 通过两边添加指定的填充字符让字符串居中
print('12:')
x = "The Middle by Jimmy Eat World".center(39, "*")
print(x)

# 13、find 查找指定字串，找到返回第一个字符的索引，没有返回-1
print('13:')
title = "Monty Python's Flying Circus"
print(title.find('Python'))
print(title.find('learn'))
# find可以指定索引的起点和终点（可选参数）
print(title.find('python', 0, 10))

# 14、join  合并字符串列表
print('14:')
dirs = '', 'usr', 'bin', 'env'
print('/'.join(dirs))
print('C:' + '\\'.join(dirs))

# 15、lower 返回字符串的小写版本
# 此处想到了一个场合： 输入验证码不区分大小写，是不是不管你输入什么，都转换为小写了？
print('15:')
print('BoB Tom Peter'.lower())

# 16、replace 查找并替换指定字串
print('16:')
print('this is a test'.replace('is', 'eez'))
print('我们'.replace('我', '你'))

# 17、split 拆分字符串，默认在空白处拆分
print('17:')
print('usr/bin/env'.split('/'))

# 18、strip 删除开头和末尾的空白  lower处的想法： 假定用户不小心在末尾加上了空格，就可以用这个方法避免报错
print('18:')
x = '   internal whitespace is kept   '.strip()  # 也可以指定要删除的开头结尾内容
print(x)

# 19、translate 单字符的替换
# 使用之前需要建立一个转换表
print('19:')
table = str.maketrans('cs', 'kz')
x = 'this is an incredible test'.translate(table)
print(x)
# 调用方法maketrans时，第三个可选参数为指定删除的字母
table = str.maketrans('cs', 'kz', ' ')
x = 'this is an incredible test'.translate(table)
print(x)

# 补充：以is打头的方法用于判断字符串是否具有某种特定的性质
