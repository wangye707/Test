#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 二进制中1的个数.py
# @Author: WangYe
# @Date  : 2019/6/19
# @Software: PyCharm

def NumberOf1(n):
    # write code here
    list1 = []
    if n >= 0:
        shang = n
        while shang:
            yushu, shang = key(shang)
            list1.append(yushu)
        cishu = 0
        for k in list1:
            if k == 1:
                cishu = cishu + 1
        print(list1)
        return cishu
    else:
        shang = -1 * n
        while shang:
            yushu, shang = key(shang)
            list1.append(yushu)
        print(list1)
        for k in range(len(list1)):
            if list1[k] == 1:
                list1[k] = 0
            else:
                list1[k] = 1
        up =1
        for k in range(len(list1)):
            p = k
            list1[p],up = change(list1[p], up)
        cishu = 1
        for k in list1:
            if k == 1:
                cishu = cishu + 1
        # print(list1)
        return cishu


def key(num):
    shang = int(num / 2)
    yushu = num - (shang * 2)
    return yushu, shang


def change(num, up):
    num = num + up
    if num == 2:
        return [0, 1]
    else:
        return [num, 0]

NumberOf1(-10)