#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : tencent 11111111.py
# @Author: WangYe
# @Date  : 2019/9/1
# @Software: PyCharm

if __name__ == '__main__':
    s1 = [int(i) for i in input().split(' ')]
    t = s1[0]
    k = s1[1]

    for i in range(t):
        s2 = [int(i) for i in input().split(' ')]
        a = s2[0]
        b = s2[1]
        sum1 = 0
        for j in range(a,b+1):
            if j< k :
                sum1 = sum1 + 1
                continue
            else:
                sum1 = sum1 + 1
                for x in range(k,j+1,k):
                    sum1+=j+1-x
        print(sum1)
# for i in range(0,10,2):
#     print(i)

# include<iostream>
# include<string.h>
# include<vector>
# include<map>

