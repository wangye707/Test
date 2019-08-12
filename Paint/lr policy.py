#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : lr policy.py
# @Author: WangYe
# @Date  : 2019/7/30
# @Software: PyCharm
import matplotlib.pyplot as plt
from pylab import *

x = np.linspace(0,6000)
y = 0.1*((1-(x/6000))**2)
# plt.figure(1)
plt.xlabel("iteration")
plt.ylabel("learning rate")
# plt.ylim(-0.1, 1)
# plt.title(r"$f(x) = sin^2(x-2)e^{-x^2}$")
plt.title(r"poly lr")
# plt.title(r"$f(x) = 0.1*(1-x/6000)^{2}$")
plt.plot(x,y)
plt.show()


# import matplotlib.pyplot as plt
# from pylab import *
#
# x = np.linspace(0,6000,500)
#
# y = []
# for i in x:
#     if i<1500:
#         y.append(0.1)
#     if (i>=1500 and i<3000):
#         y.append(0.01)
#     if (i >= 3000 and i < 4500):
#         y.append(0.001)
#     if (i>=4500 and i<=6000):
#         y.append(0.0001)
# # plt.figure(1)
# plt.xlabel("iteration")
# plt.ylabel("learning rate")
# # plt.ylim(-0.1, 1)
# # plt.title(r"$f(x) = sin^2(x-2)e^{-x^2}$")
# plt.title(r"poly lr")
# # plt.title(r"$f(x) = 0.1*(1-x/6000)^{2}$")
# plt.plot(x,y)
# plt.show()