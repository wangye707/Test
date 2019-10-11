#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 122. 买卖股票的最佳时机 II.py
# @Author: WangYe
# @Date  : 2019/9/21
# @Software: PyCharm
a = [1,2,3]
print(a[-2::-1])
# def maxProfit(prices):
#     def go(nums, oo):
#         k = 0
#         if len(nums) < 3:
#             return oo
#         else:
#             pre = float('inf')
#             out = 0
#             for i in range(len(nums)):
#                 pre = min(pre, nums[i])
#                 if nums[i] - pre > out:
#                     out = nums[i] - pre
#                     # print(k)
#                     k = i
#             oo = oo + out
#             # print(k,oo)
#             return go(nums[k:], oo)
#
#     oo = 0
#     return go(prices, oo)
# print(maxProfit([7,1,5,3,6,4]))