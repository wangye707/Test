#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 迷宫.py
# @Author: WangYe
# @Date  : 2019/8/24
# @Software: PyCharm
if __name__ == '__main__':
    num = int(input())
    strr = []
    for i in range(num):
        if i == 0:
            nums = [int(i) for i in input().split(' ')]
        else:
            strs = [i for i in input().split(' ')]
            strr.append(strs)

    out = []
    for i in range(num):
        if i %2 ==0:
            out.append('Yes')
        else:
            out.append('No')
    print('\n'.join(out))