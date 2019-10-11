#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 438.找到字符串中所有字母异味词.py
# @Author: WangYe
# @Date  : 2019/9/25
# @Software: PyCharm
def findAnagrams(s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    out = []
    need = {}
    for i in p:
        if i in need:
            need[i] += 1
        else:
            need[i] = 1
    l = len(p)
    win = {}
    for i in range(len(s)-l+1):
        if i ==0:
            win = {}
            for k in s[i:i + l]:
                if k in win:
                    win[k] += 1
                else:
                    win[k] = 1
        else:
            # print(s[i-1],win)
            if win[s[i-1]] >1:
                win[s[i-1]] -=1
            else:
                del win[s[i-1]]
            if s[i+l-1] in win:
                win[s[i+l-1]] +=1
            else:
                win[s[i+l-1]] = 1
        if win==need:
            out.append(i)
    return out
s = "cbaebabacd"
p = "abc"
print(findAnagrams(s,p))