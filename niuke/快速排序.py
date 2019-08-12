#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 快速排序.py
# @Author: WangYe
# @Date  : 2019/7/18
# @Software: PyCharm
a = [1,2,3,4,5,6]
# a = [1 for i in range(10)]
print(a.insert(0,0))
print(a)


def quick_sort(L):
    return q_sort(L, 0, len(L) - 1)

def q_sort(L, left, right):
    if left < right:
        pivot = Partition(L, left, right)

        q_sort(L, left, pivot - 1)
        q_sort(L, pivot + 1, right)
    return L

def Partition(L, left, right):
    pivotkey = L[left]

    while left < right:
        while left < right and L[right] >= pivotkey:
            right -= 1
        L[left] = L[right]
        while left < right and L[left] <= pivotkey:
            left += 1
        L[right] = L[left]

    L[left] = pivotkey
    return right

L = [5, 9, 1, 11, 6, 7, 2, 4]

print(quick_sort(L))