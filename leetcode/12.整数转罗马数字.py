#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 12.整数转罗马数字.py
# @Author: WangYe
# @Date  : 2019/8/19
# @Software: PyCharm
def intToRoman(num):
    values = [1000, 900, 500, 400,
              100, 90, 50, 40,
              10, 9, 5, 4,
              1]
    symbols = ['M', 'CM', 'D', 'CD',
               'C', 'XC', 'L', 'XL',
               'X', 'IX', 'V', 'IV',
               'I']
    out = ''
    index = 0
    while index < 13:
        if num >= values[index]:
            out = out + symbols[index]
            num = num - values[index]
            # continue
        else:
            index +=1
    return out
print(intToRoman(59))

