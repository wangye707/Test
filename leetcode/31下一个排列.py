#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 31下一个排列.py
# @Author: WangYe
# @Date  : 2019/9/21
# @Software: PyCharm
def nextPermutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in range(len(nums) - 1, 0, -1):
        for k in range(i - 1, -1, -1):
            if nums[k] < nums[i]:
                nums[i], nums[k] = nums[k], nums[i]
                return nums
    return nums[::-1]
print(nextPermutation([1,3,2]))