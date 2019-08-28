#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : kuaishou.py
# @Author: WangYe
# @Date  : 2019/8/25
# @Software: PyCharm
# def go(s: str):
#     if not s: return 0
#     wy = 0
#     qq = 0
#     lookup = set()
#     n = len(s)
#     max_len111 = 0
#
#     for i in range(n):
#         wy += 1
#         while s[i] in lookup:
#             lookup.remove(s[qq])
#             qq += 1
#             wy -= 1
#         if wy > max_len111: max_len111 = wy
#         lookup.add(s[i])
#     return max_len111
# if __name__ == '__main__':
#     s = input()
#     print(go(s))

# def s(str1, tar='X'):
#     r = eval(str1.replace('=', '-(') + ')', {tar:1j})
#     try:
#         out = -r.real / r.imag
#     except:
#         return -1
#     else:
#         return int(out)
# if __name__ == '__main__':
#     s1 = input()
#     print(s(s1))
def go(length,N,s):
    out = []
    first = 0
    for i in range(len(s)):
        if 'P' in s[i]:
            first = i
            break
    out = out + s[:first+1]
    n = int(N/2)
    v = []
    p = []
    for i in s[first+1:]:
        if 'P' in i:
            p.append(i)
        else:
            v.append(i)
    # print(p)
    vi = 0
    pi = 0
    #print(v)
    #print(p)
    while 1:
        #print(out)
        if ('P' in out[-1]):
            for k in range(n):
                try:
                    out.append(v[vi])
                    #print('122')
                except:
                    return out
                else:
                    vi = vi + 1
                #print('111',out)
        else:
            try:
                out.append(p[pi])
            except:
                return out
            else:
                pi = pi + 1

if __name__ == '__main__':
    N = int(input())
    length = int(input())
    list1 = []
    for i in range(length):
        list1.append(input())
    qq = go(length=length,N=N,s=list1)
    print(len(qq))
    for i in qq:
        print(i)
