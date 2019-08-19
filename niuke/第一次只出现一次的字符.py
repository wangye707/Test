#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 第一次只出现一次的字符.py
# @Author: WangYe
# @Date  : 2019/8/12
# @Software: PyCharm
# def FirstNotRepeatingChar( s):
#     # write code here
#     out = {}
#     for i in s:
#         if i not in out:
#             out[i] = 1
#         else:
#             out[i] += 1
#     a = []
#     for k, v in out.items():
#         if v == 1:
#             a.append(s.index(k))
#     return sorted(a)[0]
# print(FirstNotRepeatingChar(s='google'))

def FirstNotRepeatingChar( s):
    # write code here
    out = {}
    for i in s:
        if s.count(i) ==1:
            return s.index(i)
print(FirstNotRepeatingChar(s='google'))