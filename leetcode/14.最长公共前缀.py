#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 14.最长公共前缀.py
# @Author: WangYe
# @Date  : 2019/8/19
# @Software: PyCharm
def longestCommonPrefix(strs):
    if not strs: return ""
    s1 = min(strs)
    s2 = max(strs)
    for i,x in enumerate(s1):
        if x != s2[i]:
            return s2[:i]
    return s1


print(longestCommonPrefix(["flower","flow","flight"]))
