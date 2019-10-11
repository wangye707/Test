#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 当当.py
# @Author: WangYe
# @Date  : 2019/9/2
# @Software: PyCharm
# num = [int(i) for i in input().split(',')]
# for i in range(len(num)):
#     if 0 == num[i]:
#         num.pop(i)
#         num.insert(0,0)
#     if 2 == num[i]:
#         num.pop(i)
#         num.insert(-1,2)
# str1 = ''
# for i in num:
#     str1 = str1 + str(i) + ','
# print(str1[0:-1])
# str = '0,0,1,1,2,2'

def quicksort(nums):
    if len(nums) <= 1:
        return nums

    # 左边数组
    left = []
    # 右边数组
    right = []
    # 基准数
    base = nums.pop()

    # 对原数组进行划分
    for x in nums:
        if x < base:
            left.append(x)
        else:
            right.append(x)

    # 递归调用
    return quicksort(left) + [base] + quicksort(right)

if __name__ == '__main__':
    num = [int(i) for i in input().split(',')]
    # print(quicksort(num))
    str1 = ''
    for i in quicksort(num):
        str1 = str1 + str(i) + ','
    print(str1[:-1])

