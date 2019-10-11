#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 360笔试题.py
# @Author: WangYe
# @Date  : 2019/8/31
# @Software: PyCharm
# from collections import Counter
# def go(str1):
#     return Counter(str1).most_common()[0][1]
# if __name__ == '__main__':
#     s = input()
#     print(go(s))
def liqingpei(N,M,list1):
    out_position = []
    for i in range(N+1):
        temp = [i]
        for j in list1:
            for k in temp:
                if (j+k) > 0 and (j+k) <10:
                    temp.append((j+k))
                if (k-j) > 0 and (k-j) <10:
                    temp.append((k-j))
                #if not (j+k) > 0 and (j+k) <10 and not (k-j) > 0 and (k-j) <10:
                del temp[temp.index(k)]
        out_position.append(temp)
    out = 0
    for i in out_position:
        if len(i)>0:
            out = out + 1
    return out


if __name__ == '__main__':

    ll = input().split(' ')
    number = int(ll[0])
    moment = int(ll[1])
    temp_list1 = []
    for i in range(moment):
        temp_list1.append(int(input()))
    print(liqingpei(number,moment,temp_list1))

