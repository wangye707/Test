#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 67. 二进制求和.py
# @Author: WangYe
# @Date  : 2019/9/19
# @Software: PyCharm
def addBinary(a, b):
    return bin(int(a,2)+int(b,2))[2:]