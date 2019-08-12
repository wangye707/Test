#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 111111.py
# @Author: WangYe
# @Date  : 2019/8/11
# @Software: PyCharm
# cishu = int(input())
# str_list = []
# for i in range(cishu):
#     str_list.append(input())
def do(str1):
    big_list = ''
    for i in range(len(str1)):
        temp = []
        out_list = []
        if str1[i] == 'N':
            temp.append(1)
        else:
            temp.append(-1)
        for i in range(len(temp)):
            k = 0
            if temp[i] > 0:
                n = n +1
        #     big_list.append(i)

    return big_list
# def cha(big_list):
print(do('NNNNNRNR'))