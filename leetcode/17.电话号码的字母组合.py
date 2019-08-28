#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 17.电话号码的字母组合.py
# @Author: WangYe
# @Date  : 2019/8/20
# @Software: PyCharm
def letterCombinations(digits):
    m = {
        '2': 'abc', '3': 'def', '4': 'ghi',
        '5': 'jkl', '6': 'mno', '7': 'pqrs',
        '8': 'tuv', '9': 'wxyz'
    }
    if len(digits) == 1:
        return [i for i in m[digits]]
    if len(digits) == 0:
        return []

    def go(str1, str2):
        out = []
        for i in range(len(str1)):
            for j in range(len(str2)):
                temp = str1[i] + str2[j]
                out.append(temp)
        return out

    # print(m['2'])
    out = []

    res = []
    for i in digits:
        out.append(m[i])
    print(out)
    for i in m[digits[0]]:
        res.append(i)
    for i in range(1,len(out)):
        res = go(res, out[i])

    return res



print(letterCombinations(''))
# print(["ad","ae","af","bd","be","bf","cd","ce","cf","ag","ah","ai","bg","bh","bi","cg","ch","ci","dg","dh","di","eg","eh","ei","fg","fh","fi"])