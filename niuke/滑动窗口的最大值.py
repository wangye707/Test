#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 滑动窗口的最大值.py
# @Author: WangYe
# @Date  : 2019/8/13
# @Software: PyCharm
def maxInWindows(num, size):
    # write code here

    out = []
    k = len(num) - size + 1
    for i in range(k):
        out.append(max(num[i:i + size]))
    return out
print(maxInWindows(num=[2,3,4,2,6,2,5,1],size=3))