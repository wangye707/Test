#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 插入排序.py
# @Author: WangYe
# @Date  : 2019/7/18
# @Software: PyCharm
def insertionSort(arr):
    for i in range(len(arr)):
        preIndex = i-1
        current = arr[i]
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex+1] = arr[preIndex]
            preIndex-=1
        arr[preIndex+1] = current
    return arr