# #! E:\Program\anaconda python
# # -*- coding:utf-8 -*-
# # datetime:2020/3/24 21:08
# 寻找n以内的亲密数对。 代码格式如下： def fac(n): ... return xxx n = int(input()) # 此处输入由系统自动完成不需要自己输入，只要写这样一条语句即可 ...（3分）
#
# 题目内容：
# 对于两个不同的整数A和B，如果整数A的全部因子（包括1，不包括A本身）之和等于B；且整数B的全部因子（包括1，不包括B本身）之和等于A，则将A和B称为亲密数。自定义函数fac(x)计算x包括1但不包括本身的所有因子和并返回。从键盘输入整数n，调用fac()函数寻找n以内的亲密数并输出。注意每个亲密数对只输出一次，小的在前大的在后，例如220-284。
# 输入格式:
# 按提示用input()函数输入
# 输出格式：
# 按样例形式，可使用形如“print("{}-{}".format(参数1, 参数2))”输出语句进行亲密数对的输出
# 输入样例：
# 500
# 输出样例：
# 220-284
import math


def fac(x):
    """计算一个数的所有因子和 超过一半就不用
    检索了 减少运算"""
    i = 2
    p_sum = 1
    while i <= (x // 2):
        if x % i == 0:
            p_sum += i
        i += 1

    return p_sum


def anl_prime(n):
    """判断是否为素数 减少运算量"""
    if n == 1:
        return False

    n_prime = int(math.sqrt(n))

    for i in range(2, n_prime + 1):
        if n % i == 0:
            return False
    return True


def pairs(n):
    """找亲密对 从4开始"""
    try:
        filter_1 = [i for i in range(4, n + 1) if anl_prime(i) != 1]

        for i in filter_1:
            prb = fac(i)

            # 排除可能： 因子之和超出范围或者刚好是本身
            if prb not in filter_1 or i == prb:
                continue
            if fac(prb) == i:
                print('{}-{}'.format(i, prb))
                # 找到之后就从亲密对列表删除 保证数对的唯一
                filter_1.remove(i)
    except Exception as e:
        raise e


if __name__ == '__main__':
    test = int(input())
    pairs(test)

#
# import math
#
#
# def fac(n):
#     i = 2
#     divisor_num = 1
#     while i <= n // 2:
#         if n % i == 0:
#             divisor_num += i
#         i += 1
#     # print('{}的因子之和为:{}'.format(n, divisor_num))
#     return divisor_num
#
#
# # 判断是否为素数
# # a的所有正因子和等于b，b的所有正因子和等于a，因子包括1但不包括本身，且a不等于b，则称a，b为亲密数对
# # 按照亲密数对的定义，任意素数的全部因子之和都是1，很明显不应该构成亲密数对
# def isPrime(n):
#     if n == 1:
#         return False
#     square_root = int(math.sqrt(n))
#     for i in range(2, square_root + 1):
#         if n % i == 0:
#             return False
#     return True
#
#
# def getNumberPairs(n):
#     try:
#         # 获取包括n以内的合数-->素数不构成亲密数对
#         temp = [i for i in range(4, n + 1) if isPrime(i) != 1]
#         for i in temp:
#             j = fac(i)
#             # 如果因子之和等于本身，则不会构成亲密数对
#             if j not in temp or i == j:
#                 continue
#             if fac(j) == i:
#                 print('{}-{}'.format(i, j))
#                 # 将其从temp列表删除，为了保证每个亲密数对只输出一次
#                 temp.remove(i)
#     except Exception as e:
#         raise e
#
#
# n = int(input())
# getNumberPairs(n)
