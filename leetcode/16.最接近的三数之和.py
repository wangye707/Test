#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 16.最接近的三数之和.py
# @Author: WangYe
# @Date  : 2019/8/20
# @Software: PyCharm
def threeSumClosest(nums,target):
    nums.sort()
    out = 10000
    for i in range(len(nums)-2):
        j = i+1
        k = len(nums)-1
        while j<k:
            temp = nums[i] + nums[j] + nums[k]
            # print(out,temp)
            if abs(temp-target) < abs(target-out):
                out = temp
            # print(temp)
            if temp < target:
                # out = temp
                j = j +1
            elif temp > target:
                k = k - 1
            elif temp == target:
                return target
    return out
print(threeSumClosest([1,1,1,0],100))