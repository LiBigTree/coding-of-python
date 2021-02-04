def doc_test():
    a = """\
    123 \
    456
    789
    """
    print(a)


def zip_t():
    a = [1, 2, 3]
    b = ['one', 'two', 'three']
    for m, n in zip(a, b):
        print('{0}的英文是{1}'.format(m, n))


if __name__ == '__main__':
    # doc_test()
    # 列表推导式的使用
    # vec = [-4, -2, 0, 2, 4]
    # [x*2 for x in vec]
    # Out[3]: [-8, -4, 0, 4, 8]
    # [x for x in vec if x >= 0]
    # Out[4]: [0, 2, 4]
    zip_t()
