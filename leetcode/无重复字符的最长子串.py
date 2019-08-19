#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 无重复字符的最长子串.py
# @Author: WangYe
# @Date  : 2019/8/13
# @Software: PyCharm
def lengthOfLongestSubstring(s):
    out = ''
    if s=='':
        return 0
    for i in range(len(s)):
        temp = ''
        for k in s[i:]:
            if k in temp:
                if len(temp) > len(out):
                    out = temp
                break
            if k not in temp:
                temp = temp + k
                # continue

            if len(temp) > len(out):
                out = temp

    return len(out)
print(lengthOfLongestSubstring("pwwkew"))