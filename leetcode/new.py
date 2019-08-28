#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : new.py
# @Author: WangYe
# @Date  : 2019/8/20
# @Software: PyCharm
# if __name__ == "__main__":
#     s = input()
#     m = s.split()
#     for k in range(len(m)):
#         if len(m[k])%2 == 0:
#             continue
#         else:
#             m[k] = m[k][::-1]
#     print(' '.join(m))

# def numDecodings(s):
#     pp,p = 1,int(s[0]!='0')
#     for i in range(1,len(s)):
#         pp,p = p,pp * (9<int(s[i-1:i+1])<=26)+p*(int(s[i])>0)
#     return p
# if __name__ == '__main__':
#     s = input()
#     print(numDecodings(s))
# import numpy as np
# def go(filter,arr,m,w,h):
#     res = [0,0],[0,0]
#     np.array(res)
#     temp = 0
#     for i in range(0,m+h-1):
#         for j in range(0,m+w-1):
#             for mm in range(0,m):
#                 for n in range(0,m):
#                     if(i-mm)>=0 and (i-mm)<h and (j<n)>=0 and (j-n)<w:
#                         temp += filter[mm][n]*arr[i-mm][j-n]
#             res[i][j] = temp
#     return res
# filter = [[1,1],[1,1]]
# arr = [[1,1],[1,1]]
# m = 2
# w =2
# h = 2
# print(go(filter,arr,m,w,h))
#
# # [h,w] = fm.shape
# # q = [[1,2,3,4],[4,5,6,4],[7,8,9,4],[7,8,9,4]]
# # m = [[1,1],[1,1]]
# # np.array(q)
# # np.array(m)
# # # print(q)
# # for i in range(0,1):
# #     for j in range(0,1):
#
# import numpy as np
# def go(filter,arr,m,w,h):
#     res = [0,0],[0,0]
#     np.array(res)
#     temp = 0
#     for i in range(0,m+h-1):
#         for j in range(0,m+w-1):
#             for mm in range(0,m):
#                 for n in range(0,m):
#                     if(i-mm)>=0 and (i-mm)<h and (j<n)>=0 and (j-n)<w:
#                         temp += filter[mm][n]*arr[i-mm][j-n]
#             res[i][j] = temp
#     return res
def go(filter,arr,m,w,h):
    # res = [0,0],[0,0]
    # np.array(res)
    res = []
    for i in range(w-m+1):
        temp = []
        for j in range(h -m+1):
            temp.append(0)
        res.append(temp)
    # print(res)
    temp = 0
    for i in range(1,h-w+1):
        for j in range(1,m-w+1):
            for mm in range(1,m):
                for n in range(1,m):2
                    if(i-mm)>=0 and (i-mm)<h and (j<n)>=0 and (j-n)<w:
                        temp += filter[mm][n]*arr[i-mm][j-n]
            res[i][j] = temp
    return res
if __name__ == '__main__':
    s = input().split()
    h = int(s[0])
    w = int(s[1])
    arr = []
    for i in range(h):
        arr.append([int(i) for i in input().split()])
    m = int(input())
    filter = []
    for i in range(m):
        filter.append([float(i) for i in input().split()])
    print(go(filter,arr,m,w,h))