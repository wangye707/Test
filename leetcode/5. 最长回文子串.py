#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 5. 最长回文子串.py
# @Author: WangYe
# @Date  : 2019/8/14
# @Software: PyCharm
'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
def longestPalindrome(s):
    if s == '':
        return ''
    out = ''
    for i in range(len(s)):
        temp = ''
        m = s[i:]
        for k in range(len(m)):
            if temp == '':
                temp = temp + m[k]
            else:
                if m[k] != temp[0]:
                    temp = temp + m[k]
                else:
                    temp = temp + m[k]
                    if len(temp) > len(out):
                        if go(temp):
                            out = temp
                    # if len(m) > (k + 1):
                    #     if m[k + 1] != m[k]:
                    #         if go(temp):
                    #             break

            if len(temp) > len(out) and go(temp):
                out = temp
    # if out ==s:  #注意，是子串
    #     return s[0]
    # else:
    return out
def go(s):
    # if len(s) == 1:
    #     return True
    flag = True
    if len(s)%2==0:
        q = int(len(s)/2)
    else:
        q = int(len(s)/2)
    for i in range(q):
        if s[i] == s[len(s)-i-1]:
            # print(s[i],s[len(s)-i-1],i,-i)
            flag = True
        else:
            flag = False
            break
    return flag

print(longestPalindrome('anana'))
print(go('anana'))
