#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 正则表达式匹配.py
# @Author: WangYe
# @Date  : 2019/8/13
# @Software: PyCharm
'''
请实现一个函数用来匹配包括'.'和'*'的正则表达式。
模式中的字符'.'表示任意一个字符，
而'*'表示它前面的字符可以出现任意次（包含0次）。
 在本题中，匹配是指字符串的所有字符匹配整个模式。
 例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，
 但是与"aa.a"和"ab*a"均不匹配
'''

import re
def match(s, pattern):
    q = re.findall(pattern, s)
    print(q)
    if s in q:
        return True
    else:
        return False
match(s='aaaaaa',pattern='a*')
# def match(s, pattern):
# # write code here
#     for i in range(len(s)):
#         if s[i] == pattern[i]:
#             # s = s[1:-1]
#             # pattern = pattern[1:-1]
#             continue
#         else:
#             if pattern[i] == '*':
#                 if pattern[i-1] == s[i-1] and s[i-1] == s[i]:  #如果s前后都相等且pattern中出现*
#                     if len(s) == (i+1):
#                         pattern = pattern[0:i]+s[i-1]
#                     else:
#                         pattern = pattern[0:i]+s[i-1]+pattern[i:]
#                 if pattern[i-1] == s[i-1] and s[i-1] != s[i]:  #当 pattern 中相同的补齐之后
#                     if pattern[i+1]:
#                         pattern = pattern[0:i]+pattern[i+1:]
#                     else:
#                         pattern = pattern[0:i]
#                 #
#                 # if len(s) ==i+1:
#                 #     if len(pattern) == len(s)+2:
#                 #         if pattern[i+2] =='*':
#                 #             pattern = pattern[0:i]
#                 #
#                 # if pattern[i] != s[i]:  #s循环完了  abd  和  abc*d 这种情况
#                 #     if pattern[i+1] == '*':
#                 #         pattern = pattern[0:i] + pattern[i + 2:]
#
#
#             if pattern[i] == '.':
#                 if len(pattern) == (i+1):
#                     pattern = pattern[0:i] + s[i]
#                 else:
#                     pattern = pattern[0:i] +s[i] + pattern[i+1:]
#     print(pattern)
#     if pattern == s:
#         return True
#     else:
#         return False
# print(match(s='abd',pattern='abc*d'))


