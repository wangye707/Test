#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : lqp.py
# @Author: WangYe
# @Date  : 2019/12/20
# @Software: PyCharm

import numpy as np
a = [[1,1,1],[1,1,1],[1,1,1]]
temp = np.asarray(a).reshape(3,3,1)
print(temp.shape)
'''*******'''
tt = temp.reshape(3,3)
out = []
out.append(tt)
out.append(tt)
out.append(tt)
out = np.asarray(out).reshape(3,3,3)
print(out.shape)
