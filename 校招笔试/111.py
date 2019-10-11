#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 111.py
# @Author: WangYe
# @Date  : 2019/8/243
# @Software: PyCharm

def go(num,list1):
    out = 100
    list1.sort()
    # print(list1)
    for i in range(num+1-3):
        # print(list1[i:i+3])
        if min(list1[i:i+3])<out and min(list1[i:i+3])!=0:
            out = min(list1[i:i+3])
    return out
if __name__ == '__main__':
    cishu = int(input())
    for i in range(cishu):
        s =[int(i) for i in input().split(' ')]
        print(go(num=s[0],list1=s[1:]))
        # print(s[1:])
    #print(go(num=4,list1=[0,2,3,99]))

