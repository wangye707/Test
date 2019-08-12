#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : test11.py
# @Author: WangYe
# @Date  : 2019/7/31
# @Software: PyCharm
import copy
a = [5,1,2,3]
b = copy.deepcopy(a)
b.sort()
print(a)