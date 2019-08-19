#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 7.整数反装.py
# @Author: WangYe
# @Date  : 2019/8/15
# @Software: PyCharm
def reverse(x):
    if x>0:
        out = int(str(x)[::-1])
        if out> (2**31 - 1):
            return 0
        else:
            return out
    if x == 0:
        return 0
    if x<0:
        out = int(str(x)[0] + str(x)[:0:-1])
        if out< -(2**31 - 1):
        # return str(x)[:0:-1]

            return 0
        else:
            return out
print(reverse(-1534))
# print('-123'[3:0:-1])