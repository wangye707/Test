#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 机器人的活动范围.py
# @Author: WangYe
# @Date  : 2019/8/13
# @Software: PyCharm
def movingCount(threshold, rows, cols):
    # write code here
    m = 0
    for i in range(1,threshold+1):
        for k in range(1,rows+1):
            if sum(check(i))+sum(check(k))<=cols:
                print('i',i,k)
                m+=1

    return m

def check(num):
    out =[]
    length = len(str(num))
    for i in range(length):
        out.append(int(str(num)[i]))
    return out
print(movingCount(5,10,10))