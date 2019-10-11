#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 排列组合.py
# @Author: WangYe
# @Date  : 2019/9/5
# @Software: PyCharm
a = ['1','2','3','4','5','6']
out = []


def permute(nums):
    res = []
    def backtrack(nums, tmp):
        if not nums:
            res.append(tmp)
            return
        for i in range(len(nums)):
            backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])
    backtrack(nums, [])
    return res
print(permute(a))

