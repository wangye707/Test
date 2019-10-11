#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 53. 最大子序和.py
# @Author: WangYe
# @Date  : 2019/9/15
# @Software: PyCharm
def maxSubArray(nums):
    """
        1. dp问题. 公式为: dp[i] = max(nums[i], nums[i] + dp[i - 1])
        2. 最大子序和 = 当前元素自身最大, 或者 包含之前后最大
    """
    for i in range(1, len(nums)):
        # nums[i-1]代表dp[i - 1]
        nums[i] = max(nums[i], nums[i] + nums[i - 1])

    return nums


print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
