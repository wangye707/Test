#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 9. 字母异位词分组.py
# @Author: WangYe
# @Date  : 2019/9/12
# @Software: PyCharm
def groupAnagrams(strs):
    def compare(str1, str2):
        if len(str1) == len(str2):
            if sorted(str1) == sorted(str2):
                return True
            else:
                return False
        else:
            return False
    out = []
    pos = []
    i = 0
    while i < len(strs):
        if i in pos:
            i +=1
            continue
        # print(i)
        pos.append(i)
        temp = []
        temp.append(strs[i])
        # print(temp)
        for k in range(i,len(strs)):
            if k in pos:
                continue
            if compare(temp[0],strs[k]):
                pos.append(k)
                temp.append(strs[k])
        out.append(temp)
        i +=1

    return out
print(groupAnagrams(["boo","bob"]))
