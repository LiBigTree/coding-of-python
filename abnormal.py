#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/7 14:12
# @FileName: abnormal.py
# @Software: PyCharm

# 本篇主题： 异常处理机制
# 内容： 创建和引发异常，以及各种异常处理方式

# 1、要引发异常，可使用raise语句 可将类作为实例触发
print('1:')
# raise Exception('hyperdrive overload')

# 2、自定义异常类：从内置异常类继承

# 3、捕获异常：
print('3:')
# try:
#     x = int(input('Enter the first number:'))
#     y = int(input('Enter the second number:'))
#     print(x / y)
# except ZeroDivisionError:
#     print("The second number can't be zero!")

# 4、捕获异常后重新引发，继续向上传播
print('4: ')


class MuffledCalculator:
    muffled = False

    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print('Division by zero is illegal')
            else:
                raise


calculator = MuffledCalculator()
print(calculator.calc('10 / 2'))
# # 没有抑制异常时：
# calculator.calc('10/0')
# #抑制：
# calculator.muffled = True
# calculator.calc('10/0')

# 用raise...from...提供自己的异常上下文

# 5、except子句可以添加多个，或者一个except子句添加元组指定异常
print('5:')
# try:
#     x = int(input('Enter the first number:'))
#     y = int(input('Enter the second number:'))
#     print(x / y)
# # except ZeroDivisionError:
# #     print("The second number can't be zero!")
# # except TypeError:
# #     print("That wasn't a number,was it?")
# except (ZeroDivisionError, TypeError, NameError) as e:
#     print(e)
#     print('Your numbers were bogus...')

# 6、什么都不写：捕获所有的异常
print('6: ')
#
# try:
#     x = int(input('Enter the first number:'))
#     y = int(input('Enter the second number:'))
#     print(x / y)
# except:
#     print('Your numbers were bogus...')
# # 没有出现异常时，执行一个代码块很有用，添加else语句
# else:
# print('It went as planned')

# 7、finally子句： 发生异常时执行清理工作，这个子句非常适合确保文件或网络套接字等得以关闭
# try expect finally else 可以共存

# 8、只是想发出警告，可使用模块warnings中的函数warn
