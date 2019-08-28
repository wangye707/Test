#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 723糖果消消乐.py
# @Author: WangYe
# @Date  : 2019/8/24
# @Software: PyCharm
def candyCrush(board):
    m = len(board)
    if m == 0:
        return board
    n = len(board[0])
    if n == 0:
        return board
    todo = True
    while todo:
        todo = False
        for i in range(m):
            for j in range(n - 2):
                if board[i][j] != 0 and abs(board[i][j]) == abs(board[i][j + 1]) == abs(board[i][j + 2]):
                    board[i][j] = board[i][j + 1] = board[i][j + 2] = -abs(board[i][j])
                    todo = True
        for j in range(n):
            for i in range(m - 2):
                if board[i][j] != 0 and abs(board[i][j]) == abs(board[i-1][j]) == abs(board[i + 1][j]) == abs(board[i + 2][j]):
                    board[i][j] = board[i-1][j] = board[i + 1][j] = board[i + 2][j] = -abs(board[i][j])
                    todo = True
        for j in range(n):
            wptr = m - 1
            for i in range(m - 1, -1, -1):
                if board[i][j] > 0:
                    board[wptr][j] = board[i][j]
                    wptr -= 1
            for i in range(0, wptr + 1):
                board[i][j] = 0
    k = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != 0:
                k = k +1
    if k==candyCrush(board[0])[0] == k:
        return  board[0]
    else:
        candyCrush(board[0]),k
# a = [[3 ,1 ,2, 1, 1],[1, 1, 1, 1, 3],[1, 1, 1 ,1 ,1],[1, 1, 1 ,1 ,1],[3, 1 ,2 ,2 ,2]]
# print(candyCrush(a))
if __name__ == '__main__':
    i = 5
    in_l = []
    #list1 = ([int(i) for i in input().split(' ')])
    for m in range(5):
        list1 = ([int(i) for i in input().split(' ')])
        in_l.append(list1)
    # print()
    print(candyCrush(in_l))
    '''
    3 1 2 1 1
1 1 1 1 3
1 1 1 1 1
1 1 1 1 1
3 1 2 2 2'''