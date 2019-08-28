#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 完全平方数.py
# @Author: WangYe
# @Date  : 2019/8/19
# @Software: PyCharm
def go(n,list1):
    # list1.sort()
    out = []
    for i in range(n):
        loc = [i]
        m= [list1[i]]
        while len(loc)<n:
            for j in range(n):

                if j in loc:
                    continue
                else:
                    temp = (m[-1] + list1[j]) ** 0.5
                    if temp-int(temp) ==0:
                        m.append(list1[j])
                        loc.append(j)
                    if n==len(m):
                        out.append(m)
                        break
                    if temp-int(temp) !=0:
                        continue
            break
    return len(out)
# print(go(3,[3,6,10]))
if __name__ == '__main__':
    s = int(input())
    l = list(input())
    go(s,l)