#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 198. 打家劫舍.py
# @Author: WangYe
# @Date  : 2019/9/24
# @Software: PyCharm
def rob(nums):
    out = [0, 0, 0, 0]

    for i in range(len(nums)):
        out.append(nums[i] + max(out[:-1]))
    return max(out)
print(rob([3,1,3,9,3,5]))