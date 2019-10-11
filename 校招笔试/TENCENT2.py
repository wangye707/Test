#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : TENCENT2.py
# @Author: WangYe
# @Date  : 2019/9/1
# @Software: PyCharm


def go(n,str1,str2):
    s1 = len(str1)
    s2 = len(str2)
    while s1 < s2:
        str1 = str1 + str1
        s1 = len(str1)

    if str1[:n] == str2:
        return 1
    else:
        return 0

if __name__ == '__main__':
    n = int(input())
    str2 = input()
    k = int(input())
    out = 0
    for i in range(k):
        str1 = input()
        out = out + go(n=n,str1 = str1,str2=str2)
    print(out)

















