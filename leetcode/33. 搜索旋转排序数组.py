#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 33. 搜索旋转排序数组.py
# @Author: WangYe
# @Date  : 2019/8/28
# @Software: PyCharm
def search(nums, target):
    if len(nums) == 1 and target==nums[0]:
        return 0
    if target in nums:
        t = nums.index(target)
        # print(nums[t+1]<nums[t])
        if nums[t-1] >nums[t]:
            return t
        else:
            return -1
    else:
        return -1
nums = [3,1]
target = 1
print(search(nums,target))