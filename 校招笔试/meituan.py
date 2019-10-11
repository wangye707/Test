#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : meituan.py
# @Author: WangYe
# @Date  : 2019/8/22
# @Software: PyCharm
# def go(str1,str2):
#     l1 =len(str1)
#     l2 = len(str2)
#     l = min(l1,l2)
#     out = 0
#     for i in range(l):
#         if str1[i] == str2[i]:
#             out = out +1
#         else:
#             break
#     return out
# if __name__ == '__main__':
#     num = int(input())
#     list1 = []
#     for i in range(num):
#         list1.append(input())
#     while 1:
#         temp = [int(i) for i in input().split()]
#         print(go(list1[temp[0]-1],list1[temp[1]-1]))
# '''
# 4
# abcdefg
# acdef
# acdfghijk
# cdfg
# 1 2
# 2 3
# 3 4
# '''
def insert(arr):
    for i in range(1,len(arr)):
        j = i -1
        key = arr[i]
        while j>=0:
            if arr[j]<key:
                arr[j+1]=arr[j]
                arr[j] = key
            j -=1
    return arr
# print(insert(['']))
def go(str1):
    list1 = [i for i in str1.split(',')]
    list1 =insert(list1)
    return list1
if __name__ == '__main__':
    str1 = input()
    print(','.join(go(str1)))
# import sys
# if __name__ == '__main__':
#
#     sys.stdout.write('2')