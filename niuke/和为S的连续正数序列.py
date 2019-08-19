#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 和为S的连续正数序列.py
# @Author: WangYe
# @Date  : 2019/8/12
# @Software: PyCharm

def FindContinuousSequence(tsum):
    # write code here
    out = []
    for i in range(tsum + 1):
        temp = []
        for k in range(i, tsum + 1):
            if sum(temp) < tsum:
                temp.append(k)
            if temp == tsum:
                out.append(temp)
                break
            if sum(temp) > tsum:
                break
        print(temp)
    return out
print(FindContinuousSequence(3))