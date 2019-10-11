#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 搜狗.py
# @Author: WangYe
# @Date  : 2019/9/8
# @Software: PyCharm
num = int(input())
dic = []
def go(num):
    back = {}
    for i in range(1,num):
        out = [i]

        # k = 1
        for k in range(1,num):
            if str([k,i]) in back.keys():
                # print(back[i,k])
                dic.append(back[str([k,i])])
                continue

            # print(i,k)
            # print(out)
            out.append(k)
            while out[-1] <num:
                t =  out[-1]+out[-2]
                if t == num:
                    # print(out)
                    dic.append(len(out)+1)
                    # back[len(out)+1]=[i,k]
                    back.update({str([i,k]):len(out)+1})
                    out = out[:1]
                    # return out
                    # k = num
                    break
                elif t <num:
                    out.append(t)
                else:
                    out = out[:1]
                    # k = num
                    break
            #k = k + 1
    return dic
        #break
dic1 = go(num)
# print(dic1)
for i in set(dic1):
    print(i,dic1.count(i))
#
# a  =[3,4,4,4,4]
# q = set(a)
# print(q )
# a = {1:2}
# print(a)

