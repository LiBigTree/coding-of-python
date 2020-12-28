import sys


def skill_for():
    # 如果想要在循环中修改集合，可以在遍历同一个集合时通过修改遍历的副本或创建的新集合来实现
    # Iterate over a copy
    users = {'a': 'active', 'b': 'inactive', 'c': 'active'}
    for user, status in users.copy().items():
        if status == 'inactive':
            del users[user]

    print(users.items())
    # Create a new application
    active_users = {}
    for user, status in users.items():
        if status == 'active':
            active_users[user] = status
    print(active_users.items())


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
