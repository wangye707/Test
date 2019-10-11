#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : DUOYI.py
# @Author: WangYe
# @Date  : 2019/9/2
# @Software: PyCharm
for i in range(10000,99999):
    k = str(i)
    if int(k[0])%3==0 and int(k[0]+k[1]) %5 ==0 and int(k[0]+k[1]+k[2]) %7 ==0 and int(k[0]+k[1]+k[2]+k[3]) %6 == 0 and i%14==0:
        print(i)

