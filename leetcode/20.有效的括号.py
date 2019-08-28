#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 20.有效的括号.py
# @Author: WangYe
# @Date  : 2019/8/27
# @Software: PyCharm
def go(str1):
    #栈的思想
    dd = {'(':')','{':'}','[':']'}
    stack = []
    for i in str1:
        if len(stack)!= 0:
            try:

                dd[stack[-1]]
            except:
                stack.append(i)
            else:
                if dd[stack[-1]] == i:
                    print(dd[stack[-1]])
                    stack.pop()
                else:
                    stack.append(i)
        else:
            stack.append(i)
    if len(stack)==0:
        return True
    else:
        return False
print(go(str1="[)"))

