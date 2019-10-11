#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 路虎.py
# @Author: WangYe
# @Date  : 2019/9/5
# @Software: PyCharm
# s1 = input().split(' ')
# n = int(s1[0])
# m = int(s1[1])#数的数字
# a = [int(i) for i in input().split(' ')]
# w = [int(i) for i in input().split(' ')]
#
# def qunzhong(w):
#     sum_w = sum(w)
#     for i in range(len(w)):
#         w[i] = w[i]/sum_w #W是权重百分比
#     return w
# gailu = []
# out = []#a，
# def go(a,w,out):
#     if len(a) == 1:
#         if a[0] == 1:#好人赢了
#             p = 1
#             for i in out:
#                 p = p *i[1]
#             gailu.append(p*w[0])
#             return
#     for i in range(len(a)):
#         ii = ((i+m-1)%(len(a)+1))
#         print(i,ii)
#         out.append([a.pop(ii),w.pop(ii)])
#         w = qunzhong(w)
#         go(a=a,w = w,out = out)
# go(a,w,out)
# print(out)
'''
3 2
0 0 1
2 1 1
'''
#
# num = int(input())
# list1 = [int(i) for i in input().split(' ')]
# # list1.sort()
# def pij(num,i,j):
#     # print(num,i,j)
#     return max(num[i:j+1])
# def go(list1):
#     out = []
#     # for i in range(num):
#     #     out.append(pij(list1,i,num-1))
#     #     out.append(pij(list1,0,num-1-i))
#     # return sum(out)
#     for i in range(num):
#         for j in range(num-1,i-1,-1):
#             if i==j:
#                 out.append(pij(list1,i,j))
#                 break
#             else:
#                 out.append(pij(list1,i,j))
#                 # out.append()
#     if sum(out) > 1000000007:
#         return sum(out)%1000000007
#     else:
#         return sum(out)
# print(go(list1))
'''
3
1 2 2
'''
num = int(input())
list1 = []
for i in range(num):
    list1.append([int(k) for k in input().split(' ')])
def is_ok(list1):
    for i
