#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 6.Z 字形变换.py
# @Author: WangYe
# @Date  : 2019/8/15
# @Software: PyCharm
'''
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zigzag-conversion
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
#核心思想   每次  2*numRows -2个字符
def convert(s, numRows):
    if numRows <=1:
        return s
    if numRows == 2:
        s1 = s[::2]
        s2 = s[1::2]
        s3 = s1 + s2
        return s3
    res = [''] * numRows
    i = 0
    n = len(s)
    while i<n:
        print(i)
        if i>n:
            break
        for k in range(numRows):  #列的坐标
            if i<n:
                res[k]=res[k]+s[i]
                i = i +1
        for k in range(numRows-2,0,-1):  #方向，从下往上
            if i<n:
                res[k] = res[k] + s[i]
                i=i+1
    return ''.join(res)

print(convert("LEETCODEISHIRING",3))

