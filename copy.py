#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : copy.py
# @Author: WangYe
# @Date  : 2019/7/17
# @Software: PyCharm
import copy
a = [1,2]
b = [1,copy.copy(a)]
a[0]=2
print(b)