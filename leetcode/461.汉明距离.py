#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 461.汉明距离.py
# @Author: WangYe
# @Date  : 2019/9/26
# @Software: PyCharm
# def hammingDistance(x, y):
#     """
#     :type x: int
#     :type y: int
#     :rtype: int
#     """
x = 1
y = 4
x1 = bin(x)[2:]
y1 = bin(y)[2:]
if len(x1)>len(y1):
    for i in range(len(x1)-len(y1)):
        y1 = '0' + y1
elif len(x1)<len(y1):
    for i in range(len(y1)-len(x1)):
        x1 = '0' + x1
out = 0
for i in range(len(x1)):
    if x1[i]!=y1[i]:
        out = out +1
print(out)
# print(x1)
# print(y1)