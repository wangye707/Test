#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : d.py
# @Author: WangYe
# @Date  : 2019/8/10
# @Software: PyCharm

def GetResult(k):
    out = 0
    now = []  #是否换位
    for i in range(len(k)):
        now_list = k[i]
        df= now_list[0]
        dj = now_list[1]
        cha = now_list[-1]
        next_list = k[i+1]
        nf = next_list[0]
        nj= next_list[1]
        cha = next_list[-1]
        if (df + nf)<(dj+nj+cha):
            now.append(0)
            out += df
        elif (df + nf)>(dj+nj+cha):
            now.append(1)
            out += nf
# ******************************结束写代码******************************


_K = int(input())
m = []
for i in range(_K):
    temp = list(input())
    m.append(temp)
res = GetResult(m)

print(res, "\n")