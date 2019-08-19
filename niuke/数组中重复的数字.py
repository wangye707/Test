#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 数组中重复的数字.py
# @Author: WangYe
# @Date  : 2019/8/13
# @Software: PyCharm
def duplicate(numbers, duplication):
    # write code here
    for i in numbers:
        if numbers.count(i) != 1:
            duplication.append(i)
            return duplication[0]
print(duplicate(numbers=[2,1,3,1,4],duplication=[]))
