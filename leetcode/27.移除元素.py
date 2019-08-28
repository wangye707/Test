#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 27.移除元素.py
# @Author: WangYe
# @Date  : 2019/8/28
# @Software: PyCharm
def removeElement(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            del nums[i]
        else:
            i += 1
    return len(nums)
n = [0,1,2,2,3,0,4,2]
v = 2
print(removeElement(nums=n,val=v))