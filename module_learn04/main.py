# import fibo
# from fibo import fib

print("导入了main...")
from . import fibo

# if __name__ == '__main__':
    # # 访问做好的模块
    # fibo.fib(1000)
    # print(fibo.fib2(100))
    # # 当前模块的名称
    # print(fibo.__name__)
    # print(__name__)

    # 导入模块，赋值简化方便后续使用
    # fib = fibo.fib
    # fib(500)

    # 模块中的变量
    # print(fibo.var_module)

    # 脚本方式执行模块
    # import sys
    #
    # fib(int(sys.argv[1]))
