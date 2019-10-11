#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : zenjoy.py
# @Author: WangYe
# @Date  : 2019/9/20
# # @Software: PyCharm
# def convert(s, numRows):
#     if numRows <= 1:
#         return s
#     if numRows == 2:
#         s1 = s[::2]
#         s2 = s[1::2]
#         s3 = s1 + s2
#         return s3
#     res = [''] * numRows
#     i = 0
#     n = len(s)
#     while i < n:
#         # print(i)
#         if i > n:
#             break
#         for k in range(numRows):  # 列的坐标
#             if i < n:
#                 res[k] = res[k] + s[i]
#                 i = i + 1
#         for k in range(numRows - 2, 0, -1):  # 方向，从下往上
#             if i < n:
#                 res[k] = res[k] + s[i]
#                 i = i + 1
#     return ''.join(res)
# ss = input().split(' ')
# s = ss[0]
# n = int(ss[1])
# print(convert(s,n))
# import copy
# s = input()
# q=[]
# for i in s:
#     q.append(i)
# l = []
# for i in q:
#     if i not in l:
#         l.append(i)
# ll = len(l)
# d = {}
# k = 0
# print()
# for i in range(len(q)):
#     if q[i] not in d:
#         if k == 1:
#             k = k +1
#             continue
#         if i == 0:
#             d[q[i]] = 1
#         else:
#             d[q[i]] = k
#             k = k +1
# out = ''
# for i in q:
#     out = out + str(d[i])
# print(int(out,ll))

a = {1:2,3:4}
print(a.values())