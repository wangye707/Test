#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 79. 单词搜索.py
# @Author: WangYe
# @Date  : 2019/9/4
# @Software: PyCharm
def exist(board, word):
    l = len(board)
    h = len(board[0])

    def go(i, j, word,mark):
        #print(i,j)
        if ([i,j] not in mark) and i<=(l-1) and i>=0 and j<=h-1 and j>=0:
            if len(word) == 1:
                if board[i][j] == word:
                    # print(111111, board[i][j], [i, j],mark)
                    return True
                else:
                    return False
            else:
                if board[i][j] == word[0]:
                    if ([i,j] not in mark):
                        mark.append([i,j])
                        #if i <= l-1 and j <= h-1 and i>=0 and j>=0:
                        if go(i+1, j, word[1:],mark) or go(i, j+1, word[1:],mark) or go(i-1 , j, word[1:],mark) or go(i , j-1,word[1:],mark):
                            # print(i, j, board[i][j], mark)
                            # print(go(i+1, j, word[1:],mark) or go(i, j+1, word[1:],mark) or go(i-1 , j, word[1:],mark) or go(i , j-1,word[1:],mark))
                            # F = go(i+1, j, word[1:],mark) or go(i, j+1, word[1:],mark) or go(i-1 , j, word[1:],mark) or go(i , j-1,word[1:],mark)
                            return True
                            # return go(i+1, j, word[1:],mark) or go(i, j+1, word[1:],mark) or go(i-1 , j, word[1:],mark) or go(i , j-1,word[1:],mark)
                        else:
                            print(111,i,j,mark)
                            temp.remove([i, j])
                            return False
                    else:
                        return False
                else:

                    return False
        else:
            return False

    out = []
    for i in range(l):
        for j in range(h):
            if board[i][j] == word[0]:
                temp = []
                out.append(go(i,j,word,temp))
    return True in out
# board  =[
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# word = "SEE"
board = [["A","B","C","E"],
         ["S","F","E","S"],
         ["A","D","E","E"]]

word = "ABCESEEEFS"
print(exist(board = board ,word=word))
