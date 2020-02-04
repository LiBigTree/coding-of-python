# 从数据类型篇进入语句控制篇
# 本篇概览： 先了解一些编程技巧>> print、import、序列解包、链式赋值、增强赋值、代码块，
# 然后进入控制语句的学习>> 条件和条件语句（布尔值、if、else、elif、嵌套、运算符）、断言、
# 循环（while、for、迭代字典）、跳出循环、循环中的else子句、简单推导、三人行（pass、del、exec（eval））

# ----------1、print-------------
# 可以打印多个参数
print('1:')
greeting = 'Hello'
salutation = 'Mr.'
name = 'Gumby'

print(greeting + ',', salutation, name)
# 可以自定义分隔符
print(greeting + ',', salutation, name, sep="_")

# 可以自定义结束字符串（默认是换行符）
print('Hello,', end='')
print('world!')

# ---------2、import----------------
# import 用来导入模块:
# import somemodule
# from somemodule import somefunction
# from somemodule import somefunction, anotherfuction, yetanotherfunction
# from somemodule import *
# --------------------------------------------------------------------
# 两个模块都有一个函数，则：
# module1.open(...)
# module2.open(...)

# 或者用as指定别名
print('2: ')
import math as foobar
print(foobar.sqrt(4))

# from module1 import open as open1
# from module2 import open as open2

# 3、序列解包: 将一个序列（或者任何可迭代对象解包，并将得到的值储存到一系列变量中）
print('3.1:')
x, y, z = 1, 2, 3
print(x, y, z)
x, y = y, x
print(x, y, z)
# 在使用返回元组（可迭代对象）时很有用——
print('3.2: ')
scoundrel = {'name': 'Robin', 'girlfriend': 'Marion'}
key, value = scoundrel.popitem()

print(key)
print(value)

# 解包两边元素个数要相等，若不相等，可使用*来收集多余的值。
# 用带星号*收集的变量最后总是包含一个列表
print('3.3: ')
a, b, *rest = [1, 2, 3, 4]
print(rest)

a, *b, c = "abc"
print(a, b, c)

# 4、链式赋值
# 即 x = y = somefunction() 等价于：
# y = somefuction()
# x = y

# 5、 增强赋值
# + — * / %
# x = x + 1 >> x += 1

# 6、代码块
# 代码块是一组语句，在满足条件时执行（if for 等等）
# 在python中代码块通过冒号指出，通过缩进内容来表达

# -------条--件--语--句--------------

# 7、布尔值 bool
# 假： False None 各种类型的0 空序列、空映射（"" () [] {}）
# 真： True 除了假
print(bool('I think, therefore I am'))

# 假值之间不等价： [] != ""
# 8、bool >> if（-else）语句
# print('8: ')
# name = input('what is your name?')
# if name.endswith('Gumby'):
#     print('hello, Mr.Gumby')
# else:
#     print('Hello, friends!')

# 引申： if条件表达式： 三目运算符
status = "friends" if name.endswith("Gumby") else "stranger"

# 9、elif子句
print('9: ')
# num = int(input('Enter a number:'))
# if num > 0:
#     print('The number is positive')
# elif num < 0:
#     print('The number is negative')
# else:
#     print('The number is zero')

# 代码块之间也可以嵌套

# 10、关于条件本身——运算符
# 比较运算符： ==、 <、 >、 >=、 <=、 !=、 is、 is not、in、not in

# 关于 == 和 is：
# == 判断两个对象是否相等， is是检查两个对象是否相同——即指向同一个地址

# in： 成员资格运算符

# 关于字符串和序列比较：
# 根据字符串字母排列顺序逐个比较>>获悉字母顺序值用ord
print(ord("a"))

# 关于布尔运算符： and、 or、 not
# 特征： 只做必要的运算——短路逻辑 and 找到False就返回， or找到True就返回

# 11、断言：让程序在错误条件出现时立即崩溃
# 使用关键字 assert
age = 10
assert 0 < age < 100
age = 1
assert 0 < age < 100, 'The age must be realistic'
print('come here')
# 断言之后就不往下执行了

# --------------循--------环-------------------
# 12、while循环
print('12: ')
x = 1
while x <= 3:
    print(x)
    x += 1

# 13、for循环： 为序列中每个元素执行代码块
print('13: ')
words = ['this', 'is', 'an', 'ex', 'parrot']
for word in words:
    print(word)

# 一般，只要能够使用for循环，就不用while循环

# 14、迭代字典（在for循环中可用序列解包）
d = {'x': 1, 'y': 2, 'z': 3}
for key, value in d.items():
    print(key, 'corresponds to', value)
# 字典顺序是不确定的，顺序很重要--处理方法是 将键或值储存在一个列表，用模块collections中的OrderDict类排序，再进行迭代。

# 15、一些迭代工具

# 15.0、对于迭代（遍历），在python中有一个内置函数
print(list(range(0, 10)))
# 范围类似于切片--（start, end, stride）,包含起点不包含结束。

# 15.1： zip 并行迭代, 用于缝合序列--当序列长度不同时，zip在最短的序列用完后停止
print('15.1: ')
names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]
for name, age in zip(names, ages):
    print(name, 'is', age, 'years old')
print(list(zip(names, ages)))

# 15.2 enumerate 迭代时获取索引
print('15.2:')
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))

for index, season in enumerate(seasons):
    if 'Fall' in season:
        seasons[index] = "秋天"
        print(seasons)

# 15.3、反向迭代：reversed 排序迭代：sorted
print('15.3: ')

print(sorted([4, 3, 6, 8, 3]))
print(list(reversed('hello world!')))

# 16、跳出循环

# 16.1 break 结束循环
print('16.1: ')
from math import sqrt
for n in range(99, 0, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        print('here')
        break

# 16.2 continue 结束当前迭代

# 16.3 while True/break
# 例子：
# while True:
#     word = input('Please enter a word: ')
#     if not word:
#         break
#     print('the word was', word)

# 17、跳出循环
# 法一： 可在循环开始前定义一个布尔变量并将其设置为Fasle，再在跳出循环的条件处设置为True
print('17: ')
break_out = False
for n in range(99, 81, -1): # 为了对比测试法二的else子句，将下限改成了81
    root = sqrt(n)
    if root == int(root):
        print(n)
        break_out = True
        break
if not break_out:
    print("I didn't break out!")
# 法二： else子句也能达到上述效果， 而且代码更加简洁
for n in range(99, 81, -1): # 为了对比测试法二的else子句，将下限改成了81
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
else:
    print("I didn't break out!")

# 18、简单推导： 列表推导，从其他列表创建列表
print('18: ')
print([x*x for x in range(10)])

# 可以加if
print([x*x for x in range(10) if x % 3 == 0])

# 可以加更多的for
print([(x, y) for x in range(3) for y in range(3)])
# 对比:
result = []
for x in range(3):
    for y in range(3):
        result.append((x, y))
print(result)

# 例子： 首字母相同的男女名字配对
girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']

letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0], []).append(girl)
    # print(letterGirls)
print([b+'+'+g for b in boys for g in letterGirls[b[0]]])

# 字典推导
squares = {i: "{} squared is {}".format(i, i**2) for i in range(10)}
print(squares[8])

# 19、pass
# 一个占位符，什么也不做
# 场景举例： 编写if语句时，一个代码块暂时出不来，就先pass占着位置

# 20、del
# 删除不再用的变量值

# 21、exec、eval
# exec： 将字符串作为代码执行，exec提供一个参数时是全局变量>>所以要有命名空间
# eval： 计算用字符串表示的python表达式的值，并返回结果
