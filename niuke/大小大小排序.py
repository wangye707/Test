#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 大小大小排序.py
# @Author: WangYe
# @Date  : 2019/5/21
# @Software: PyCharm

in_data = input()
data = in_data.split(',')
out = []   #输出列表

def compare(num1,num2):  #比较函数
    if num1 > num2:
        return 0
    if num1 < num2:
        return 1
    if num1 == num2:
        return 2

for k in range(len(data)):

    if k == 0:  #存入首位
        out.append(int(data[k]))
    else:
        num1 = int(data[k-1])
        num2 = int(data[k])

        if (k%2) == 0:
            if compare(num1,num2) == 1:
                out.append(num2)
                out[k-1],out[k] = out[k],out[k-1]   #元素交换
            else:
                out.append(num2)
        else:
            if compare(num1, num2) == 0:
                out.append(num2)

                out[k - 1], out[k] = out[k], out[k - 1]  # 元素交换
            else:
                out.append(num2)

print(out)

