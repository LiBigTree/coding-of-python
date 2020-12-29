def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("after local: ", spam)
    do_nonlocal()
    print("after nonlocal: ", spam)
    do_global()
    print("after global: ", spam)


if __name__ == '__main__':
    # 理解作用域与命名空间，一个命名空间下的多个作用域
    scope_test()
    print("In global scope: ", spam)
