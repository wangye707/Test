#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 和为S的两个数字.py
# @Author: WangYe
# @Date  : 2019/8/12
# @Software: PyCharm
def FindNumbersWithSum(array, tsum):
    # write code here
    out = []
    for i in array[:int(len(array) / 2)]:
        if i in out:
            break
        temp = []
        if (tsum - i) in array:
            temp.append(i)
            temp.append(tsum - i)
            out.append(temp)
    if out:
        loc = []
        for k in out:
            loc.append(k[0] * k[1])

        return out[loc.index(min(loc))]

    else:
        return []
print(FindNumbersWithSum([1,2,4,7,11,15],15))

