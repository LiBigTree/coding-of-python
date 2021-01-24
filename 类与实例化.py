# class MyClass:
#     def __init__(self):
#         self.data = ['这是初始化的内容']
#     """A simple class"""
#     i = 12345
#
#     def f(self):
#         return "hello world"
#
#
# class Complex:
#     def __init__(self, realpart, imagpart):
#         self.r = realpart
#         self.i = imagpart

class Dog:
    kind = 'canine'  # class variable shared by all instance

    tricks = []

    def __init__(self, name):
        self.name = name  # instance variable unique to each variable
        # self.tricks = []

    def add_tricks(self, trick):
        self.tricks.append(trick)


class Dog2:

    def __init__(self, name):
        self.name = name  # instance variable unique to each variable
        self.tricks = []

    def add_tricks(self, trick):
        self.tricks.append(trick)


class Warehouse:
    purpose = 'storage'
    region = 'west'


if __name__ == '__main__':
    # w1 = Warehouse()
    # print(w1.purpose, w1.region)
    # print("=====前后对比=====")
    # w2 = Warehouse()
    # w2.region = 'east'
    # print(w2.purpose, w2.region)

    # 生成器表达式
    print("使用生成器表达式：", sum(i*i for i in range(10)))

    # # 共享范围对比
    # print("=== 这是放在类的共享区域里： ===")
    # d = Dog('Fido')
    # e = Dog('Buddy')
    # d.add_tricks('roll over')  # 换言之，实例将属性引用映射到了不同的位置：查找时一般时先映射到共享的类的位置，再是映射到每个实例下。
    # e.add_tricks('play dead')
    # print(d.tricks)
    # print(e.tricks)
    #
    # print("=== 这是利用初始化，为每个实例创建的空间： ===")
    # d2 = Dog2('Fido')
    # e2 = Dog2('Buddy')
    # d2.add_tricks('roll over')  # 换言之，实例将属性引用映射到了不同的位置：查找时一般时先映射到共享的类的位置，再是映射到每个实例下。
    # e2.add_tricks('play dead')
    # print(d2.tricks)
    # print(e2.tricks)

    # # 类和实例变量
    # d = Dog('Fido')
    # e = Dog('Buddy')
    # print("=== shared by all variable ===")
    # print(d.kind)
    # print(e.kind)
    # print("=== unique by each variable ===")
    # print(d.name)
    # print(e.name)

    # # 属性引用
    # # MyClass.i = 'changed' 类的属性可以被赋值，可以通过赋值来更改值
    # print(MyClass.i)  # 返回一个整数
    # print(MyClass.__doc__)
    # print(MyClass.f)  # 返回一个函数对象

    # 实例化
    # x = MyClass()
    # print(x.data)

    # # 实例化2
    # x2 = Complex(3.0, -4.5)
    # print('实数部分：%.1f；虚数部分：%.1f' % (x2.r, x2.i))

    # # 实例化的属性引用: 数据属性
    # x.counter = 1
    # while x.counter < 10:
    #     x.counter = x.counter * 2
    # print(x.counter)
    #
    # del x.counter

    # # 方法 类的属性引用叫做函数对象 实例化之后的引用叫做方法
    # xf = x.f
    # print(xf())
