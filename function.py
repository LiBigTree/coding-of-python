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
    'Caculates the square of the number x.'
    return x * x

# 访问文档字符串
print(square.__doc__)
# 内置的函数help可获取有关函数的信息，包括文档字符串

# ---------------参---数--------------------
# 编写函数： 确保在提供正确参数完成任务，参数不对时以显而易见的方式失败（断言或异常）
# 函数名后面的变量称为形参，调用函数时提供的值称为实参。
