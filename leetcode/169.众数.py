#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 169.众数.py
# @Author: WangYe
# @Date  : 2019/9/24
# @Software: PyCharm
def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dict = {}
    m = nums[0]
    for i in nums:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
            if dict[i] > dict[m]:
                m = i
    return  m
print(majorityElement([2,2,1,1,1,2,2]))