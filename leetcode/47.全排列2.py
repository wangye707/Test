#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 47.全排列2.py
# @Author: WangYe
# @Date  : 2019/9/12
# @Software: PyCharm
def permuteUnique(nums):
    out = []
    def go(nums,temp):
        if len(nums) == 0:
            if temp not in out:
                out.append(temp)
        else:
            for i in range(len(nums)):
                # print(type(nums))
                go(nums[:i]+nums[i+1:],temp + [nums[i]])
    temp = []
    go(nums,temp)
    return out
print(permuteUnique([1,1,2]))