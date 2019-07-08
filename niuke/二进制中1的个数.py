#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 二进制中1的个数.py
# @Author: WangYe
# @Date  : 2019/6/19
# @Software: PyCharm

# def NumberOf1(n):
#     # write code here
#     list1 = []
#     if n >= 0:
#         shang = n
#         while shang:
#             yushu, shang = key(shang)
#             list1.append(yushu)
#         cishu = 0
#         for k in list1:
#             if k == 1:
#                 cishu = cishu + 1
#         list1.reverse()
#         print(list1)
#
#
# def key(num):   #求除以2之后的余数和商
#     shang = int(num / 2)
#     yushu = num - (shang * 2)
#     return yushu, shang
#
# #
# # def change(num, up):
# #     num = num + up
# #     if num == 2:
# #         return [0, 1]
# #     else:
# #         return [num, 0]
#
# NumberOf1(10)
def NumberOf1(n):
    count = 0
    for i in range(32):

        count += (n >> i) & 1
        print('i', i,count)
    # print(count)
NumberOf1(10)