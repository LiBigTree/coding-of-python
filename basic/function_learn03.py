# 学习python中的函数部分

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()  # 空行


# 对一个或多个参数指定默认值
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


i = 5


def f(arg=i):
    print(arg)


def f2(a, one=[]):
    # 测试默认值执行的次数
    one.append(a)
    return one


def f3(a, eli_one=None):
    if eli_one is None:
        eli_one = []
    eli_one.append(a)
    return eli_one


def parrot(voltage, state='a stiff', action='vcom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


def cheese_shop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


def standard_arg(arg):
    print(arg)


def pos_only_arg(arg, /):
    print(arg)


def kwd_only_arg(*, arg):
    print(arg)


def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


if __name__ == '__main__':
    # 不同调用方式比对
    standard_arg(2)
    pos_only_arg(1)  # 希望形参名称对用户不可用时使用、对API，防止形参名称修改时造成破坏性的API变动
    kwd_only_arg(arg=2)  # 形参有实际意义、防止过度依赖传入参数的位置时
    combined_example(1, 2, kwd_only=3)


    # 简单的定义与调用函数
    # fib(100)

    # ask_ok函数的调用方法
    # ask_ok('Do you really want to quit?')  # 只给出必需的参数
    # ask_ok('OK to overwrite the file?', 2)  # 给出一个可选的参数
    # ask_ok('OK to overwrite the file?', 2, reminder='Come on, only yes or no!')

    # 默认值的调用位置
    # i = 6
    # f()

    # # 测试默认值参数调用次数
    # print(f2(1))
    # print(f2(2))
    # print(f2(3))
    # print(f3(1))
    # print(f3(2))
    # print(f3(3))

    # # 关键字参数的学习
    # parrot(1000)  # 1 positional argument
    # print()
    # parrot(voltage=2000)  # 1 keyword argument
    # print()
    # parrot(voltage=1000, action='VOOOOOM')  # 2 keyword arguments
    # print()
    # parrot(action='VOOOOOM', voltage=1000) # 2 keyword arguments
    # print()
    # parrot('a million', 'bereft of life', 'jump')  # 3 positional arguments
    # print()
    # parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

    # # 剩余参数的收集
    # cheese_shop("Limburger", "It's very runny, sir.",
    #             "It's really very, VERY runny, sir.",
    #             shopkeep="Michael Pallin",
    #             client="John Cleese",
    #             sketch="Cheese Shop Sketch")
