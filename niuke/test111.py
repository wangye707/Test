#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : test111.py
# @Author: WangYe
# @Date  : 2019/8/11
# @Software: PyCharm
cishu = int(input())
num_list = []
count_list = []
for i in range(cishu):
    num_list.append(int(input()))
    temp = input().split()
    temp_list = []
    for i in temp:
        temp_list.append(int(i))
    count_list.append(temp_list)
    # print(count_list)

def turn_bin(num):
    num_bin = str(bin(num).replace("0b",''))
    out = 0
    for i in num_bin:
        out = out + int(i)
    return out
def do(num,count):
    same = []
    for i in range(num):
        if turn_bin(count[i]) not in same:
            same.append(turn_bin(count[i]))
    return len(same)
# print(do(num_list[0],[8,3,5,7,2]))
for i in range(cishu):
    print(do(num_list[i],count_list[i]))
