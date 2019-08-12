#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 列表的坐标排序.py
# @Author: WangYe
# @Date  : 2019/8/12
# @Software: PyCharm
def location_sort(list_in):

    max_location =sorted(enumerate(list_in), key=lambda y:y[1],reverse=True)
                   #读取坐标为 1 的数字  ，然后进行排序                #reverse是确定排序顺序的
    list_out = []
    for i in range(len(max_location)):
        list_out.append(max_location[i][0])

    return (list_out)

print(location_sort([1,3,2]))