#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 36.有效的数独.py
# @Author: WangYe
# @Date  : 2019/8/29
# @Software: PyCharm


def isValidSudoku(board):
    # flag = True

    for i in range(9):
        hang = []
        lie = []
        q_hang = i // 3
        q = []
        for j in range(9):
            q_lie = j // 3
            if board[i][j] != '.':
                if board[i][j] in hang:
                    return False
                else:
                    hang.append(board[i][j])
            if board[j][i] != '.':
                if board[j][i] in lie:
                    return False
                else:
                    lie.append(board[j][i])
            if [q_hang, q_lie] not in q:
                temp = []
                for k in range(q_hang * 3, (q_hang + 1) * 3):
                    for m in range(q_lie * 3, (q_lie + 1) * 3):
                        if board[k][m] == '.':
                            continue
                        if board[k][m] not in temp:
                            temp.append(board[k][m])
                        else:
                            return False
            else:
                continue
    return True


s = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],["6", ".", ".", "1", "9", "5", ".", ".", "."],[".", "9", "8", ".", ".", ".", ".", "6", "."],["8", ".", ".", ".", "6", ".", ".", ".", "3"],["4", ".", ".", "8", ".", "3", ".", ".", "1"],["7", ".", ".", ".", "2", ".", ".", ".", "6"],[".", "6", ".", ".", ".", ".", "2", "8", "."],[".", ".", ".", "4", "1", "9", ".", ".", "5"],[".", ".", ".", ".", "8", ".", ".", "7", "9"]]
print(isValidSudoku(s))
