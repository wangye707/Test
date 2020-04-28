#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : RNN折线图.py
# @Author: WangYe
# @Date  : 2019/3/26
# @Software: PyCharm

from pylab import *
import matplotlib.pyplot as plt
mpl.rcParams['font.sans-serif'] = ['SimHei']
y1=[20775,18644,17482,16001,15461,14772,15031,15772,16659,17856,19158]
# x1=[4,6,8,10,15,20]
x1=[1,1.2,1.4,1.6,1.8,2,2.2,2.4,2.6,2.8,3]
# x2=[1,1.2,1.4,1.6,1.8,2,2.2,2.4,2.6,2.8,3]
# # x3=[4,6,8,10,15,20]
# y2=[40775,40775,40775,40775,40775,40775,40775,40775,40775,40775,40775]
# y3=[45015,45015,45015,45015,45015,45015]
plt.plot(x1,y1
         # ,label='改进方法'
         ,linewidth=3,
         color='red',
         # marker='*',
markerfacecolor='black',
         markersize=10)
# plt.plot(x2,y2,linewidth=3,
#          label = '传统方法'
#          , color='black'
#          # ,marker='v',
# ,markerfacecolor='black',markersize=12
#          )
# plt.plot(x2,y2,label='SSGD')
# plt.plot(x3,y3,label='Single')
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('α',size = 20)
plt.ylabel('time(s)',size = 20)
plt.title('实验3中α参数对耗时的影响',size=20)
plt.legend()
plt.savefig('cifar10.svg',format = 'svg')
plt.show()
