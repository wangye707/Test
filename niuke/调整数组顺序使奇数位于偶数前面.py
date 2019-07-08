#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 调整数组顺序使奇数位于偶数前面.py
# @Author: WangYe
# @Date  : 2019/6/28
# @Software: PyCharm
def reOrderArray(array):
    # write code here
    length = len(array)
    jishu = 0
    oushu = length - 1
    new_list = []
    # k =0
    # for i in range(length):
    #     print(i)
    #     if k + i  == length + 1:
    #         break
    #     if array[i] % 2 == 0:
    #         # print(array)
    #         temp = array[i]
    #         del array[i]
    #         array.append(temp)
    #         length = length - 1
    #         i = i-1
    #     else:
    #         continue
    #     print(array)
    i =0
    while (length - i):
        if array[i] % 2 == 0:
    #         # print(array)
            temp = array[i]
            del array[i]
            array.append(temp)
            length = length - 1
            continue
        i =i+1
        print(array)
reOrderArray([1,1,1,2,3,4,5,6,7])