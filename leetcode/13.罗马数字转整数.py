#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 13.罗马数字转整数.py
# @Author: WangYe
# @Date  : 2019/8/19
# @Software: PyCharm
def romanToInt(s):
    values = [1000, 900, 500, 400,
              100, 90, 50, 40,
              10, 9, 5, 4,
              1]
    symbols = ['M', 'CM', 'D', 'CD',
               'C', 'XC', 'L', 'XL',
               'X', 'IX', 'V', 'IV',
               'I']
    num = 0
    index = 0
    length = len(s)
    while index < length:
       if index == length - 1:
           num = num + values[symbols.index(s[index])]
           index = index + 1
           break
       if symbols.index(s[index]) <= symbols.index(s[index+1]) :  #是否 前一位大于后一位
           num = num + values[symbols.index(s[index])]
           index = index +1
       else:
           num = num + values[symbols.index(s[index]+s[index+1])]
           index = index +2
    return num
print(romanToInt("III"))