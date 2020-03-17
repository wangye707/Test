#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 加速比图.py
# @Author: WangYe
# @Date  : 2019/12/16
# @Software: PyCharm
from pylab import *
import matplotlib.pyplot as plt
mpl.rcParams['font.sans-serif'] = ['SimHei']
y1=[418000,400983,384812,367900,316714,279302,292161,301580,356123,412314,510350]
y2=[1194,1096,996,806,756,622,504,659,714,801,898]
y3=[40775,38644,30482,29001,25461,21031,20001,20772,22659,27856,30158]
y4=[664,563,499,459,422,399,429,468,599,690,702]
out= []
x1=[1,1.2,1.4,1.6,1.8,2,2.2,2.4,2.6,2.8,3]
for i in range(len(y1)):
    ss = (y1[0]/y1[i] + y2[0]/y2[i] +y3[0]/y3[i] +y4[0]/y4[i] )/4
    out.append(ss)
plt.plot(x1,out,linewidth=3,color='black'
         ,marker='o',
markerfacecolor='black',markersize=5
         )
# plt.plot(x2,y2,label='SSGD')
# plt.plot(x3,y3,label='Single')
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('α',size = 20)
plt.ylabel('Rα (mean)',size = 20)
plt.title('α参数对应加速比',size=20)
plt.legend()
# plt.savefig('ff.emf')
plt.savefig('加速比.svg',format = 'svg')
plt.show()
