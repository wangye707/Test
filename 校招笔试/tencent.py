#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : tencent.py
# @Author: WangYe
# @Date  : 2019/9/1
# @Software: PyCharm
#
# def go(list1):
#     #list1.sorted()
#     # list1 = [1,1,2]
#
#     set1 = set(list1)
#     if len(set1) == 1:
#         return 'NO'
#     temp_b = []#重复
#     temp_a = []#不重复
#     for i in set1:
#         if list1.count(i) >=2:
#             temp_b.append(i)
#         else:
#             temp_a.append(i)
#     if len(temp_b)>1:
#         num1 = list1.index(temp_b[0])
#         del list1[num1]
#         num2 = list1.index(temp_b[-1])
#         del list1[num2]
#         return go(list1)
#     elif len(temp_b) == 1:
#         num1 = list1.index(temp_b[0])
#         del list1[num1]
#         num2 = list1.index(temp_a[0])
#         del list1[num2]
#         return go(list1)
#     else:
#         return 'YES'
# #print(go([4,4,4,3]))
# if __name__ == '__main__':
#     n = int(input())
#     list1 = []
#     for i in range(n):
#         n = int(input())
#         temp_list = [int(i) for i in input().split(' ')]
#         list1.append([n,temp_list])
#     for i in list1:
#         print(go(i[1]))




