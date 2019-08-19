#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 9.回文数.py
# @Author: WangYe
# @Date  : 2019/8/15
# @Software: PyCharm
def isPalindrome(x):
    n = int(len(x)/2)
    l = len(x)
    flag = False
    t=str(x)
    for i in range(n):
        # print(t[i],t[n-i-1],i,n-i-1,n)
        if t[i] == t[l-i-1]:
            # print(t[i])
            flag = True
        else:
            flag = False
            break
    return flag
print(isPalindrome('1221'))