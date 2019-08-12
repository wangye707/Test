#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 两数之和.py
# @Author: WangYe
# @Date  : 2019/8/12
# @Software: PyCharm
"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
def twoSum(nums, target):
    for i,v in enumerate(nums):
        if (target-v) in nums:
            print([i,nums.index(target-v)])


twoSum(nums = [2, 7, 11, 15], target = 9)