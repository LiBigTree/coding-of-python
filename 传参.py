import sys


def para_test():
    """
    使用脚本传参数测试

    命令行调用，关于文档说明的书写——空格缩进不会被删除
    """
    for arg in sys.argv:
        print(arg)


def test_doc():
    # no doc
    pass


if __name__ == '__main__':
    # skill_for()
    # para_test()
    print(para_test.__doc__)
    print(test_doc.__doc__)
