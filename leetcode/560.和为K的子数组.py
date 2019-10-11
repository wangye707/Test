0#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 560.和为K的子数组.py
# @Author: WangYe
# @Date  : 2019/9/26
# @Software: PyCharm
def subarraySum(nums, k):
    out = 0
    for i in range(len(nums)):
        j = 1
        while (i + j)<len(nums):
            if nums[i] == k:
                out += 1
                # break
            nums[i] = nums[i] + nums[i + j]
            j = j +1
        if  nums[i]==k:
            out +=1
    return out
print(subarraySum([1,1,1],2))