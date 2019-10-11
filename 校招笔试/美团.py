#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 美团.py
# @Author: WangYe
# @Date  : 2019/9/5
# @Software: PyCharm
# 1： 输入一个list， 输出list，要求奇数在左，偶数在右
# 2： 输入一个字符串，返回不包含重复字符的subset 的最大长度
a = [1,2,3,4,5,6,77,8,9,46,651,654,1,61,156,18,4,1631]
for i in range(len(a)):
   if a[i] %2 == 0:
       a.insert(0,a.pop(i))
       # print(a)
   else:
       a.append(a.pop(i))
# print(a)
