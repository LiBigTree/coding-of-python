def fibonacci() -> list:
    # debug观察斐波那契数列计算过程
    a, b = 0, 1
    c = []
    while a < 1000:
        print(a, end=",")
        a, b = b, a+b
        c.append(a)
    return c


def annotations_test(ham: str, eggs: str = 'eggs') -> str:
    """
    函数标注的使用例子：其中分别有对位置参数、关键字参数、返回值的标注
    """
    print("Annotations:", annotations_test.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs


def lambda_test(n):
    return lambda x: x + n


def transport():
    pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
    pairs.sort(key=lambda pair: pair[1])
    print(pairs)


def unpack_para():
    args = [3, 6]
    show = list(range(*args))
    print(show)


if __name__ == '__main__':
    # 函数标注（和文档字符串一起学习的）
    result = annotations_test('spam')
    print(fibonacci.__annotations__)
    print(result)

    # # lambda：返回一个函数
    # f = lambda_test(42)
    # print(f(8))
    # 传递小函数作为参数
    transport()

    # 将元组里的参数**解包**分别传递给调用的函数
    # unpack_para()
