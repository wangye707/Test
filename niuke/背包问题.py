#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 背包问题.py
# @Author: WangYe
# @Date  : 2019/7/8
# @Software: PyCharm
import numpy as np

def solve(vlist,wlist,totalWeight,totalLength):
    resArr = np.zeros((totalLength+1,totalWeight+1),dtype=np.int32)
    # print(resArr)
    for i in range(1,totalLength+1): #物品数量
        for j in range(1,totalWeight+1): #背包重量
            if wlist[i] <= j:
                resArr[i,j] = max(resArr[i-1,j-wlist[i]]+vlist[i],resArr[i-1,j])
            else:                   #   重量差的价值定位
                resArr[i,j] = resArr[i-1,j]
    return resArr

if __name__ == '__main__':
    v = [3,6,5,4,6]
    w = [2,2,6,5,4]
    weight = 10
    n = 4
    result = solve(v,w,weight,n)
    print(result)