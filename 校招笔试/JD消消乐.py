#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : JD消消乐.py
# @Author: WangYe
# @Date  : 2019/8/24
# @Software: PyCharm
a = [[3 ,1 ,2, 1, 1],[1, 1, 1, 1, 3],[1, 1, 1 ,1 ,1],[1, 1, 1 ,1 ,1],[3, 1 ,2 ,2 ,2]]
def go(list1):
    hang = len(list1)
    lie = len(list1[0])
    position = []
    temp = 0
    nums = []
    for i in range(hang):
        for j in range(lie):
            if list1[i][j] not in nums:
                nums.append(list1[i][j])

    for num in nums:
        temp_position = []
        for i in range(hang):
            temp_hang = []
            for j in range(lie):

                if num == list1[i][j]:
                    temp_hang.append(1)
                else:
                    temp_hang.append(2)
            temp_position.append(temp_hang)

        i = 0
        j = 0
        while 1:
            if temp_position[i][j] ==

    # print(position)
go(list1=a)


