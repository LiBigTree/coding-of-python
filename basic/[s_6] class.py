#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/6 9:41
# @FileName: class.py
# @Software: PyCharm

# 本篇概览：
# 核心：创建自定义对象
# 1、多态、方法、继承
# 2、类（9）： 创建自定义类 > 类的属性/（函数和）方法 > 隐藏 >
# 类的命名空间 > 指定超类 > 再谈继承 > 多个超类 > 接口和内省 >
# 抽象基类

# 面向对象的设计思想是抽象出Class，根据Class创建Instance


# 1、创造类
class Person:
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def greet(self):
        print("Hello, world! I'm {}.".format(self.name))


foo = Person()
foo.set_name('lider')
foo.greet()


# 2、隐藏 私有属性 不能从外部访问
# 加 __两个下划线
# python中私有的幕后方法是对所有以两个以下划线打头的名称进行转换，即在开头加上一个下划线和类名


class Secretive:
    def __inaccessible(self):
        print("Bet you can't see me...")

    def accessible(self):
        print("The secret message is:")
        self.__inaccessible()


s = Secretive()
s.accessible()  # 不能从外部访问私有属性，但在内部仍可以使用

s._Secretive__inaccessible()  # 不应该这样做

# 3、类的命名空间
print('3:')


class MemberCounter:
    members = 0

    def init(self):
        MemberCounter.members += 1


m1 = MemberCounter()
m1.init()
print(MemberCounter.members)

m2 = MemberCounter()
m2.init()
print(MemberCounter.members)
# 上述代码在类作用域定义了一个变量，所有成员可以访问它

# 每个实例都可以访问这个类作用域的变量：
print(m1.members)
print(m2.members)

# 在实例中给属性赋值，将会遮挡类级变量（联系函数中局部变量和全局变量的关系）
m1.members = 'Two'
print(m1.members)
print(m2.members)


# 4、（子类中）指定超类： 类名后加上超类名，用圆括号括起
print('4: ')


class Filter:
    """这是超类（基类）"""
    def init(self):
        self.blocked = []

    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]


class SPAMFilter(Filter):
    """这是子类，拥有超类的所有方法，除此之外还有其需要特有的方法（也可能是重写一些既有的方法）"""
    def init(self):
        self.blocked = ['SPAM']


f = Filter()
f.init()
print(f.filter([1, 2, 3]))

s = SPAMFilter()
s.init()
print(s.filter(['SPAM', 'SPAM', 'SPAM', 'SPAM', 'eggs', 'bacon', 'SPAM']))
# 总结： 第二个从Filter基类派生，定义了init方法，利用基类的filter，达到过滤的效果。这样做的好处是无需重新编写基类已有的定义

# 5、探讨继承：
print('5:')
# 判断一个类是否是另一个子类：
print(issubclass(SPAMFilter, Filter))
# 用 __bases__知道一个类的基类
# 用 isinstance 确定对象是否是特定类的实例
# 用__class__获悉对象属于哪个类

# 6、基类可以有几个
# 7、接口和内省
# 查看对象所需的方法是否存在
# 对象中存储的所有值——检查__dict__属性
# 内省是在运行时确定对象类型的能力：dir inspect模块 type id

# 面向对象：
# 确定需要那些类以及这些类应该包含哪些方法时，可以这样：
# （1）将有关问题描述记录下来，标出所有名词、动词和形容词
# （2）名词中找出可能的类；
# （3）动词中找可能的方法；
# （4）形容词找可能的属性；
# （5）把方法和属性分配给各个类；
# >> 改进上述模型： 设想场景去考虑
