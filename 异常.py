import sys


def except_test():
    while True:
        try:
            x = int(input("please input a number: "))
            break
        except ValueError:
            print("Oops! That was no valid number. Try again...")
        except (RuntimeError, TypeError, NameError):
            pass


class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


def no_except():
    try:
        f = open('myfile.txt')
        s = f.readline()
        i = int(s.strip())
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise


def else_test():
    for arg in sys.argv[1:]:
        try:
            f = open(arg, 'r')
            print('here...')
        except OSError:
            print('cannot open', arg)
        else:
            print(arg, 'has', len(f.readlines()), 'lines')
            f.close()


def connect_except():
    try:
        raise Exception('spam', 'eggs')
    except Exception as inst:
        print(type(inst))
        print(inst.args)
        print(inst)

        x, y = inst.args  # unpack args
        print('x = ', x)
        print('y = ', y)


def this_fails():
    x = 1 / 0


def inner_test():
    try:
        this_fails()
    except ZeroDivisionError as err:
        print('Handing run-time error:', err)


def raise_again():
    try:
        raise NameError('HiThere')
    except NameError:
        print('An exception flew by!')
        raise  # 这个raise重新触发了Name Error 打印出来后面的内容


def finally_test():
    try:
        raise KeyboardInterrupt
    finally:
        print('Goodbye, world!')


def bool_return():
    try:
        return True
    finally:
        return False


def with_test():
    with open("myfile.txt", encoding='utf-8') as f:
        for line in f:
            print(line, end="")


if __name__ == '__main__':
    # with子句预定义清理操作
    with_test()

    # # finally拥有最高的优先级
    # x = bool_return()
    # print(x)

    # 定义必须在所有的情况下执行的清理操作
    # finally_test()

    # 重新引发异常
    # raise_again()

    # raise NameError

    # # 程序可以处理try子句中函数内部发生的异常
    # inner_test()

    # except可以在异常后面指定一个变量关联到实例
    # connect_except()

    # else子句测试
    # else_test()

    # 省略异常以用作通配符
    # no_except()

    # 异常测试：执行try语句，正常情况跳过except；出现异常去检测except中匹配的部分并执行，（没有时报错），执行完继续try语句
    # except_test()

    # 异常类的兼容问题: 基类兼容派生类。但是派生类不兼容基类
    # for cls in [B, C, D]:
    #     try:
    #         raise cls()
    #     except D:
    #         print("D")
    #     except C:
    #         print("C")
    #     except B:
    #         print("B")
    # # 异常覆盖
    # for cls in [B, C, D]:
    #     try:
    #         raise cls()
    #     except B:
    #         print("B")
    #     except D:
    #         print("D")
    #     except C:
    #         print("C")
