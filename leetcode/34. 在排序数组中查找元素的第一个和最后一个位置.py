#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 34. 在排序数组中查找元素的第一个和最后一个位置.py
# @Author: WangYe
# @Date  : 2019/8/28
# @Software: PyCharm
def searchRange(nums, target):
    k = []
    for i in range(len(nums)):
        if nums[i] == target:
            k.append(i)
    if len(k)>=2:
        return [k[0],k[-1]]
    else:
        return [-1,-1]
