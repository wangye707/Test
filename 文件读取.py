#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 文件读取.py
# @Author: WangYe
# @Date  : 2020/3/28
# @Software: PyCharm
# path = '11.txt'
# for i in range(6):
#     with open(path,'a') as f:
#         f.write(str(i))
#         f.close()
lo = [1,2,3,4]
with open('loss.txt','a') as  f:
    for i in range(len(lo)):
        f.write(str(lo[i])+' ')
    f.write('\n')
    f.close