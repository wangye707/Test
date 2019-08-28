#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 32. 最长有效括号.py
# @Author: WangYe
# @Date  : 2019/8/28
# @Software: PyCharm
def longestValidParentheses(s):
    k = []
    for i in s:
        if len(k) == 0:
            k.append(i)
            continue
        if k[-1] == '(' and i == ')':
            k.pop()
            continue
        else:
            k.append(i)
    return k
print(longestValidParentheses(s="()(()"))