#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 三数之和.py
# @Author: WangYe
# @Date  : 2019/8/19
# @Software: PyCharm
def threeSum(nums):
    nums.sort()
    res, k = [], 0
    for k in range(len(nums) - 2):
        if nums[k] > 0: break  # 1. because of j > i > k.
        if k > 0 and nums[k] == nums[k - 1]: continue  # 2. skip the same `nums[k]`.
        i, j = k + 1, len(nums) - 1
        while i < j:  # 3. double pointer
            s = nums[k] + nums[i] + nums[j]
            if s < 0:
                i += 1
                while i < j and nums[i] == nums[i - 1]: i += 1
            elif s > 0:
                j -= 1
                while i < j and nums[j] == nums[j + 1]: j -= 1
            else:
                res.append([nums[k], nums[i], nums[j]])
                i += 1
                j -= 1
                while i < j and nums[i] == nums[i - 1]: i += 1
                while i < j and nums[j] == nums[j + 1]: j -= 1
    return res

print(threeSum([-1, 0, 1, 2, -1, -4]))