#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 如何将语句组成函数
# 概览：
# 1、自定义函数
# 2、参数
# 3、作用域
# 4、递归

# 抽象是程序被人理解的关键所在： 人>>计算机
# 1、判断函数是否可以被调用——callable
print('1: ')
import math

x = 1
y = math.sqrt
print(callable(x))
print(callable(y))

# 2、定义一个函数 def
print('2:')


def hello(name):
    return 'Hello, ' + name + '!'


print(hello('world!'))

# 3、给函数编写文档: 1、# 2、添加独立的字符串，def语句、模块和类的开头——称作文档字符串，docstring
print('3；')


def square(x):
    """Calculates the square of the number x."""
    return x * x


# 访问文档字符串
print(square.__doc__)
# 内置的函数help可获取有关函数的信息，包括文档字符串

# ---------------参---数--------------------
# 编写函数： 确保在提供正确参数完成任务，参数不对时以显而易见的方式失败（断言或异常）
# 函数名后面的变量称为形参，调用函数时提供的值称为实参。
# 明确参数有两种形式： 位置参数和关键字参数

# 4、修改参数
print('4:')


def change(n):
    n[0] = 'Mr. Gumby'


names = ['Mrs. Entity', 'Mrs. Thing']
# change(names)
# print(names)

# 覆盖的是原列表， 如果不想原来列表改变，可以创建一个副本改动：
# n = names[:] 或者
n = names.copy()
change(n)
print(names)

# 5、修改参数——使用函数来修改数据结构
print('5: ')


# 例子： 编写一个程序，存储姓名，让用户能够根据名字、中间名找人
# 抽象的关键在于隐藏所有的更新细节


def init(data):
    """初始化数据结构"""
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}


def lookup(data, label, name):
    """获取人员姓名"""
    return data[label].get(name)


# def store(data, full_name):
#     """将人员储存到数据结构"""
#     names = full_name.split()
#     if len(names) == 2:
#         names.insert(1, ' ')
#     labels = 'first', 'middle', 'last'
#
#     for label, name in zip(labels, names):
#         people = lookup(data, label, name)
#         if people:
#             people.append(full_name)
#         else:
#             data[label][name] = [full_name]

#
# Mynames = {}
# init(Mynames)
# store(Mynames, "Magnus Lie Hetland")
# print(lookup(Mynames, 'middle', 'Lie'))
#
# store(Mynames, 'Robin Hood')
# store(Mynames, 'Robin Locksley')
# print(lookup(Mynames, 'first', 'Robin'))
# 参数不可修改时，应从函数返回所有需要的值。

# 6、关键字参数和默认值： 参数名称被指定
print('6: ')


def hello(name='world', greeting='Hello'):
    print('{}, {}!'.format(greeting, name))


hello()
# 7、收集参数 （序列解包处涉及过）
# 7.1 用 * 收集，将收集的值储存在元组里
print('7.1: ')


def print_params(title, *params):
    print(title)
    print(params)


print_params('params:', 1, 2, 3)
print_params('nothing:')  # 没有收集的参数，结果则是一个空元组

# 7.2 星号如果不放在最后，需要使用名称指定后续参数
print()
print('7.2: ')


def in_the_midddle(x, *y, z):
    print(x, y, z)


in_the_midddle(1, 2, 3, 4, 5, z=7)

# 7.3 一个星号不能收集关键字参数， 要两个星号, 而且得到的是字典
print()
print('7.3: ')


def print_params_2(**params):
    print(params)


print_params_2(x=1, y=2, z=3)


# 结合起来使用： 一个星号负责余下位置的参数收集，两个星号负责收集关键字参数，其余的对应下去


def print_params_3(x, y, z=3, *pospar, **keypar):
    print(x, y, z)
    print(pospar)
    print(keypar)


print_params_3(1, 2, 3, 6, 7, foo=1, bar=2)
# 给参数分区 (位置参数>>收集剩余参数*>>关键字参数**)
# 利用这个改进前面姓名存储
print('姓名储存改进： ')


def store(data, *full_names):
    """将人员储存到数据结构"""
    for full_name in full_names:
        names = full_name.split()
        if len(names) == 2:
            names.insert(1, ' ')
        labels = 'first', 'middle', 'last'

        for label, name in zip(labels, names):
            people = lookup(data, label, name)
            if people:
                people.append(full_name)
            else:
                data[label][name] = [full_name]


d = {}
init(d)
store(d, 'Luke Skywalker', 'Anakin Skywalker')
print(lookup(d, 'last', 'Skywalker'))

# 8、分配参数：


def add(x, y):
    return x + y


params = (1, 2)

add(*params)  # 在调用函数时 *起分配元组中参数的作用， **起分配字典中参数的作用
# >> 定义函数时， *和**分别将参数收集到元组和字典中

# ------------作---用---域----------------------
# 9、变量：指向值的名称， 这个由变量指向值的东西便被叫做 命名空间或作用域
print('9: ')
test = 3
scope = vars()
print(scope['test'])

# 在调用函数时，会创建一个新的命名空间，不会影响外部（全局）作用域的x。
# 在函数内使用的变量称为局部变量


def foo():
    x = 42


x = 1
foo()
print(x)

# 10、递归
# 递归两要素： 1） 基线条件； 2）递归条件

# 可以把递归和循环对比理解
print('10: ')


def factorial(m):
    if m == 1:
        return 1
    else:
        return m * factorial(m-1)


def factorial2(m):
    result = m
    for i in range(1, m):
        result *= i
    return result


print(factorial(10))
print(factorial2(10))

x = 4


def change(k):
    k = 3
    print(k)
# 深刻理解作用域（局部和全局）


change(x)
print(x)
