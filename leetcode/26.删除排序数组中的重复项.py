#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 26.删除排序数组中的重复项.py
# @Author: WangYe
# @Date  : 2019/8/28
# @Software: PyCharm
def removeDuplicates(nums):
    i = 1
    while i<len(nums):
        if nums[i] == nums[i-1]:
            del nums[i]
        else:
            i +=1
    return nums
print(removeDuplicates(nums=[1,1,2]))

