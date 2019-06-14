#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : ganqiong.py
# @Author: WangYe
# @Date  : 2019/5/28
# @Software: PyCharm

path = r'F:\ps\机器学习之文本分类\机器学习之文本分类\stop\stopword.txt'

with open(path) as f:
    out =f.readlines()
    print(out)