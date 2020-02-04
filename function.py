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


def store(data, full_name):
    """将人员储存到数据结构"""
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


Mynames = {}
init(Mynames)
store(Mynames, "Magnus Lie Hetland")
print(lookup(Mynames, 'middle', 'Lie'))

store(Mynames, 'Robin Hood')
store(Mynames, 'Robin Locksley')
print(lookup(Mynames, 'first', 'Robin'))
# 参数不可修改时，应从函数返回所有需要的值。

# 6、关键字参数和默认值： 参数名称被指定
print('6: ')


def hello(name='world', greeting='Hello'):
    print('{}, {}!'.format(greeting, name))


hello()
