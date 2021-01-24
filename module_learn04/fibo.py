# 学习模块的使用，构建更大项目
# 函数放在主函数之外的其他地方

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


var_module = 3
# if __name__ == '__main__':
#
#     print("我在导入时候被执行了。。。")

# 交互测试
# print("我还没变")
# print("我变了")

# 交互过程如下：
# import fibo
# 我在导入时候被执行了。。。
# 我还没变
# import fibo
# import importlib
# importlib.reload(fibo)
# 我在导入时候被执行了。。。
# 我变了

print("导入了fibo...")