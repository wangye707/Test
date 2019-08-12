#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 丑数.py
# @Author: WangYe
# @Date  : 2019/8/12
# @Software: PyCharm
'''
把只包含质因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含质因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''


# def GetUglyNumber_Solution(index):
#     # write code here
#     if index == 1:
#         return 1
#     dy = [2, 3, 5]
#     out = [1, 2, 3, 4, 5]
#     if index in out:
#         # return out[0:out.index(index)+1]
#         return index
#     if index > 5:
#         for k in range(6, 100000000):
#             if len(out) == index:
#                 # print(len(out))
#                 break
#             for i in dy:
#                 # print(i)
#                 temp = k / i
#                 if temp in out:
#                     out.append(k)
#                     break
#     return out[-1]

def GetUglyNumber_Solution(index):
    if (index <= 0):
        return 0
    uglyList = [1]
    indexTwo = 0
    indexThree = 0
    indexFive = 0
    for i in range(index - 1):
        newUgly = min(uglyList[indexTwo] * 2, uglyList[indexThree] * 3, uglyList[indexFive] * 5)
        uglyList.append(newUgly)
        if (newUgly % 2 == 0):
            indexTwo += 1
        if (newUgly % 3 == 0):
            indexThree += 1
        if (newUgly % 5 == 0):
            indexFive += 1
    return uglyList
print(GetUglyNumber_Solution(3))



