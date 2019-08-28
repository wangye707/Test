#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 18.py
# @Author: WangYe
# @Date  : 2019/8/20
# @Software: PyCharm
def fourSum(nums, target):
    length = len(nums)
    res = []
    nums.sort()
    for i in range(length-3):
        for j in range(length-1,i+1,-1):

            k = i +1
            g = j -1

            while g>k:

                temp = (nums[i]+nums[j]+nums[k]+nums[g])
                # print(i, k, g, j,temp)
                if target==temp:
                    q = [nums[i],nums[j],nums[k],nums[g]]
                    q.sort()
                    if q not in res:
                        res.append(q)
                    g = g - 1
                    k = k +1
                if target < temp:
                    g = g -1
                elif target > temp:
                    k = k +1
    return  res
nums = [-3,-1,0,2,4,5]
target = 0
print(fourSum(nums,target))