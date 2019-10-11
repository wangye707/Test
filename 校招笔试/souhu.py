#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : souhu.py
# @Author: WangYe
# @Date  : 2019/8/29
# @Software: PyCharm
def go(num,n):
    if num and len(str(n))>0:

        m = 0
        for i in range(n+1):
            for k in str(i):
                if num in k:
                    print(i)
                    m = m +1

        return m
    else:
        return 0

if __name__ == '__main__':
    x = input()
    if x:
        m = x.split(' ')
        if len(m)>1:
            print(go(m[0],int(m[1])))
        else:
            print(0)
    else:
        print(0)

# def go(n):
#     if n==1:
#         return 1
#     if n==2:
#         return 3
#     if n==3:
#         return 2
#     if n == 4:
#         return 3
#     # if n ==5:
#     #     return
# if __name__ == '__main__':
#     n = int(input())
#     print(go(n))

