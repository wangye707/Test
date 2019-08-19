#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 8.字符串转换整数(atoi).py
# @Author: WangYe
# @Date  : 2019/8/15
# @Software: PyCharm
def myAtoi(str):
    if str == '' or str == '-':
        return 0
    out = ''
    for i in str:


        if i ==' ':
            continue
        if i =='-' and len(out)==0:
            out = out + i
            continue
        if i =='-' and i in out:
            out = 0
            break
        if i =='-' and len(out)!=0:
            out = 0
            break
        out = out + i
        # print(out)
        if len(out)>=1:
            try:
                int(out)
            except:
                try:
                    int(out - out[-1])
                except:
                    out = 0
                    break
                else:
                    out = out - out[-1]
                    break
    if out == '':
        return 0
    return int(out)
print(myAtoi(' -42www'))
# print(int('-2w'))