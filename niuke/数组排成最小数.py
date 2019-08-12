#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 数组排成最小数.py
# @Author: WangYe
# @Date  : 2019/8/12
# @Software: PyCharm
lam = lambda n1,n2:min(int(str(n1)+str(n2)),int(str(n2)+str(n1)))
print(lam(1,2))