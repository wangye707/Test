#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 698. 划分为k个相等的子集.py
# @Author: WangYe
# @Date  : 2019/9/2
# @Software: PyCharm
def canPartitionKSubsets(nums, k):
    target = sum(nums)/k
    nums.sort(reverse= True)
    out = []
    def go(nums,target):
        for i in nums:
            if i == target:
                nums.remove(i)
                out.append(i)
                return out
            elif i>target:
                continue
            else:
                nums.remove(i)
                out.append(i)
                return go(nums , target - i)

        return False
    #go(nums,target)
    k = -1
    while len(nums) > 0 :
        pop = go(nums, target)
        if pop == False:
            return pop
        #print(nums)
        if len(nums) == k:
            return False

        k = len(nums)
        # for i in pop:
        #     print(i)
        #     print(nums)
         #   nums.remove(i)
    return 'True'

nums = [10,10,10,7,7,7,7,7,7,6,6,6]



#print(nums)
k = 3
print(canPartitionKSubsets(nums,k))