#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 矩形覆盖.py
# @Author: WangYe
# @Date  : 2019/6/14
# @Software: PyCharm
# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
class Solution:
    def rectCover(self, number):
        # write code here
        a = 1
        b = 0
        if number == 0:
            return 0
        for k in range(number):
            a ,b= a+b,a
        return a