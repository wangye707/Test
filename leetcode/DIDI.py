#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : DIDI.py
# @Author: WangYe
# @Date  : 2019/8/27
# @Software: PyCharm
def go(str1):
    q = str1.split(' ')
    # print(q)
    n = []
    s = []
    for i in q:
        try:
            int(i)
        except:
            s.append(i)
        else:
            n.append(int(i))
    # print(n)
    # print(s)
    position = []
    for i in range(len(s)):
        if len(position) ==0:
            position.append(i)
        if s[i-1]!='+' and s[i] == '+':
            # position.append(i)
            position = [i]
            continue
        elif s[i] == '*':
            position.append(i)
        if s[i] !=s[i-1] and len(position[:-1])>=2 and s[i-1]=='+': #算加法
            # print(position)
            n = n[:position[1]]+sorted(n[position[1]:position[-1]])+n[position[-1]:]
            # print(n)
            position = [i]
            continue
        #print(i,position,s[i],s[i-1],len(position[:-1]))
        if s[i] !=s[i-1] and len(position[:-1])>=1 and s[i-1]=='*': #算乘法
            #print(1)
            n = n[:position[0]]+sorted(n[position[0]:position[-1]+1])+n[position[-1]+1:]
            position = n
    return n,s

    #

if __name__ == '__main__':
    num = int(input())
    strs = input()
    n,s = go(str1=strs)
    # print(n)
    # print(s)
    out = ''
    for i in range(len(n)-1):
        out = out + str(n[i]) + " " + s[i] + ' '
    out = out + str(n[-1])
    print(out)
    '''
    1 + 2 + 3 + -5 * -4 + 1 
    '''
#     '''
#     6
# 3 + 2 + 1 + -4 * -5 + 1
#     '''
# a = [1,2,3,4]
# print(a[:-2])


