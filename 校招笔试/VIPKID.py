#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : VIPKID.py
# @Author: WangYe
# @Date  : 2019/9/3
# @Software: PyCharm
#
# def NumberOf1(n):
#     count = bin(n).replace('0b','')
#     return count.count('1')
#     # print(count)
# print(NumberOf1(10))
def go(list1,n):
    l = len(list1)
    new_list = []
    for i in range(l - n+1):
        temp = float(sum(list1[i:i+n])/n)
        #print(n)
        new_list.append(temp)
    return new_list
if __name__ == '__main__':
    list1 =[int(i)for i in  input().split(' ')]
    n = int(input())
    lll = (go(list1,n))
    for i in lll:
        print('%0.2f'%i,end=' ')
    #print(str(str(lll)[1:-1]).replace(',',' '))


