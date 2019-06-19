#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 斐波那契数列.py
# @Author: WangYe
# @Date  : 2019/6/13
# @Software: PyCharm
class Solution:
    def Fibonacci(self, n):
        # write code here
        n = int(n)
        list1=[0,1]
        if n == 0:
            return 0
        if n == 1:
            return 1
        for i in range(2,n+1):
            out = list1[i-1]+list1[i-2]
            list1.append(out)
        out = list1[n]
        return out