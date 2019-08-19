#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 11盛水最对的容器.py
# @Author: WangYe
# @Date  : 2019/8/19
# @Software: PyCharm
def maxArea(height):
    i,j = 0 ,(len(height)-1)
    s = 0
    while i!=j:
        print(i,j)
        if min(height[i],height[j])*(j-i) > s:
            s = min(height[i],height[j])*(j-i)
        if height[i]<=height[j]:
            i = i +1
            continue
        if height[i]>height[j]:
            j = j -1
            continue
    return s
print(maxArea([1,8,6,2,5,4,8,3,7]))