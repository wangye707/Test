#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 途家1.py
# @Author: WangYe
# @Date  : 2019/9/6
# @Software: PyCharm
s = input().split(' ')
a = (s[0])
b = int(s[1])
begin=0
temp = []
out = []

for i in a:
    temp.append(int(i))
while b:
    q = max(temp[:b+1])
    out.append(q)
    pos = temp[:b+1].index(q)
    # print(q,pos)
    b = b - pos
    # begin = pos + 1
    temp = temp[pos+1:]
# print(out)
sss = ''
for i in out:
    sss = sss+ str(i)
print(sss)
'''
92081346717538 10
'''
