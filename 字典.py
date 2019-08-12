#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 字典.py
# @Author: WangYe
# @Date  : 2019/8/12
# @Software: PyCharm
d = {}
d.update({'a':10})
d['b']=4
print(d)
math_score = {'Nelly': 89}         #创建一个班级数学成绩字典 math

math_score['Baade'] = 77                       #新增一个键值对 'Baade': 77
print(math_score)                              #{'Madonna': 89, 'Cory': 99, 'Annie': 65, 'Nelly': 89, 'Baade': 77}