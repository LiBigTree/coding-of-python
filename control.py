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

# 3、序列解包

