#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 寻找两个有序数组的中位数.py
# @Author: WangYe
# @Date  : 2019/8/14
# @Software: PyCharm
def findMedianSortedArrays(nums1, nums2):
    out = nums1 + nums2
    out.sort()
    if len(out) % 2 != 0:
        return float(out[int(len(out) / 2)])
    else:
        if len(out) == 1:
            return out[0]
        else:
            temp = int(len(out) / 2)
            return float(out[temp-1]+out[temp])/2
print(findMedianSortedArrays(nums1=[],nums2=[2,3]))