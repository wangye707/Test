#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 35. 搜索插入位置.py
# @Author: WangYe
# @Date  : 2019/8/28
# @Software: PyCharm
def searchInsert(nums, target):
    for i in range(len(nums)):
        if i == 0:
            if target <=nums[i]:
                return i
        if i == (len(nums)-1):
            if target > nums[i]:
                return len(nums)
        if target>nums[i] and target<=nums[i+1]:
            return i+1
nums = [1,3,5,6]
target = 5
print(searchInsert(nums,target))
