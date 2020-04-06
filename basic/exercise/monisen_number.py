#!/usr/bin/env python
# -*- coding:utf-8 -*-
# datetime:2020/3/24 22:47

# 题目内容：
# 找第n个默尼森数。P是素数且M也是素数，并且满足等式M=2^P-1，则称M为默尼森数。
# 例如，P=5，M=2^P-1=31，5和31都是素数，因此31是默尼森数。
# 输入格式: 
# 按提示用input()函数输入
# 输出格式：
# int类型
# 输入样例：
# 4
# 输出样例：
# 127


def prime(n):
    """

    :param n:
    :return: determine prime
    """
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        flag = False
        for i in range(2, n):
            if (n % i) == 0:
                flag = False
                break
            else:
                flag = True
        return flag


def monisen(order):
    """
    k > the quantity of the number in the list
    :param order: needed prime order
    :return: monisen number
    """
    mns_list = []
    i = 2
    k = 0
    while k < order:

        mns = 2**i - 1
        if prime(i) and prime(mns):
            mns_list.append(mns)
            k += 1
        i += 1

    return mns_list[-1]


print(monisen(int(input())))




