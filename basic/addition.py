#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/7 14:07
# @FileName: addition.py.py
# @Software: PyCharm

# 本篇概览： 几个魔法方法,__init__ 以及一些处理元素访问的方法（创建序列和映射）
# 特性和迭代器

# 1、构造函数
print('1: ')


class FooBar():

    def __init__(self):
        self.somevar = 42


f = FooBar()
print(f.somevar)

# 2、重写普通方法 重写是继承的一个重要机制
print('2:')


class A:
    def hello(self):
        print("hello,I'm A")


class B(A):
    def hello(self):
        print("hello, I'm B")


a = A()
b = B()
a.hello()
b.hello()

#  重写构造方法
# 法一： 调用未关联的超类构造函数 在子类添加基类的构造函数


# class Bird:
#
#     def __init__(self):
#         self.hungry = True
#
#     def eat(self):
#         if self.hungry:
#             print("Aaaah...")
#             self.hungry = False
#         else:
#             print('No, Thanks!')
#
#
# class SongBird(Bird):
#
#     def __init__(self):
#         Bird.__init__(self)
#         self.sound = 'Squawk!'
#
#     def sing(self):
#         print(self.sound)
#
#
# sb = SongBird()
# sb.sing()
# sb.eat()
# sb.eat()

# 法二： 在子类用函数super


class Bird:

    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("Aaaah...")
            self.hungry = False
        else:
            print('No, Thanks!')


class SongBird(Bird):

    def __init__(self):
        super().__init__()
        self.sound = 'Squawk!'

    def sing(self):
        print(self.sound)


sb = SongBird()
sb.sing()
sb.eat()
sb.eat()

# 实践编程应该选法二

# 3、基本的序列和映射指定的四个方法：
# __len__(self):  __getitem__(self, key): __setitem__(self, key, value): __delitem__(self, item):


# 4、特性：函数property
print('4: ')

class Rectangle:
    """对property的理解， 就是对类的内部空间代码的一种整合，目的是方便外部调用
    提高编程效率"""
    def __init__(self):
        self.width = 0
        self.height = 0

    def set_size(self, size):
        self.width, self.height = size

    def get_size(self):
        return self.width, self.height

    size = property(get_size, set_size)


r = Rectangle()
r.width = 10
r.height = 5
print(r.size)

r.size = 150, 100
print(r.width)

# 5、迭代器协议：
# 方法__iter__：返回一个迭代器，包含__next__的对象
print('5: ')


class Fibs:

    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        self.a, self.b = self.b, (self.a + self.b)
        return self.a

    def __iter__(self):
        return self


fibs = Fibs()

for f in fibs:
    if f > 10:
        print(f)
        break


# 通过对可迭代对象调用内置函数，可以获得一个迭代器

it = iter([1, 2, 3])
print(next(it))
print(next(it))

# 6、从迭代器创建序列


class TestIterator:
    value = 0

    def __next__(self):
        self.value += 1
        if self.value > 10:
            raise StopIteration
        return self.value

    def __iter__(self):
        return self


ti = TestIterator()
x = list(ti)
print(x)

# 生成器，无论编写什么程序，都可以完全不使用生成器

