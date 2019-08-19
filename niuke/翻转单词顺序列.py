#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 翻转单词顺序列.py
# @Author: WangYe
# @Date  : 2019/8/12
# @Software: PyCharm
def ReverseSentence(s):
    # write code here
    q= s.split(' ')
    q.reverse()
    return q
# .reverse()
print(ReverseSentence("student. a am I"))
