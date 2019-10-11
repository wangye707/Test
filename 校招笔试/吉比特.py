#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 吉比特.py
# @Author: WangYe
# @Date  : 2019/9/5
# @Software: PyCharm
s = input().split(' ')
s1 = s[0]
s2 = s[1]
out = []
def go(s1,s2,t):
    if len(s2) >len(s1):
        return 0
    temp = []
    for i in range(len(s2)):
        for k in range(t,len(s1)):
            if len(temp) == 0:
                if s2[i] == s1[k]:
                    temp.append(k)
                    break
            else:
                if k <= temp[-1]:
                    continue
                if s2[i] == s1 [k]:
                    temp.append(k)
                    break
    if len(temp) == len(s2):
        out.append(temp)
        if temp[-1]+1 >= len(s1)-1:
            return out[-1][0]+1
        else:
            go(s1,s2,temp[-1]+1)
    elif len(temp) != len(s2) and t ==0:
        return 0
    else:
        return
    return out[-1][0]+1
print(go(s1,s2,0))
# while len(go(s1,s2)) == len(s2):
#     t = go(s1,s2)
#     out.append(t[0])
#     s1 = s1[t[-1]+1:]
# print(out)
'''
abcdacd ad
'''