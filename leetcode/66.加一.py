#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 66.加一.py
# @Author: WangYe
# @Date  : 2019/9/19
# @Software: PyCharm
def plusOne(digits):
    ss = ''
    for i in digits:
        ss = ss + str(i)
    # for i in str(int(ss) + 1):
    #     print(i)
    return [int(i) for i in str(int(ss)+1)]
print(plusOne([1,2,5]))