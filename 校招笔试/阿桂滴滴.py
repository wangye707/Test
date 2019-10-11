#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 阿桂滴滴.py
# @Author: WangYe
# @Date  : 2019/9/19
# @Software: PyCharm
nm = [int(i) for i in input().split(' ')]
n = nm[0]
m = nm[-1]
car1 = []
car2 = []
for i in range(m):
    temp = [int(i) for i in input().split(' ')]
    car1.append(temp[0])
    car2.append(temp[-1])
def go(car1,car2,n):
    for i in range(1,n+1):
        if len(car1) >= len(car1):
            if i not in car1:
                car1.append(i)
            else:
                continue
            if i not in car2:
                car2.append(i)
        if len(car2) > len(car1):
            if i not in car2:
                car2.append(i)
            elif i not in car1:
                car1.append(i)
    return car1,car2
print(go(car1,car2,n))
'''
5 2
1 4
3 4
d 4
'''

