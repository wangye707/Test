#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 448. 找到所有数组中消失的数字.py
# @Author: WangYe
# @Date  : 2019/9/26
# @Software: PyCharm
def findDisappearedNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    return list(set(range(1,len(nums)+1)) - set(nums))
print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))
