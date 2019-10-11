#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 48.旋转图像.py
# @Author: WangYe
# @Date  : 2019/9/12
# @Software: PyCharm
def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix[0])
    # transpose matrix
    for i in range(n):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

            # reverse each row
    for i in range(n):
        matrix[i].reverse()
    return matrix
marr =[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
print(rotate(marr))