# https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        l = []
        s = []
        for i in range(9):
            l.append([])
            s.append([])
        for i in range(9):
            for j in range(9):
                l[i].append(board[j][i])
        m = n = 0
        for k in range(1,10):
            m = ((k-1)//3)*3
            for i in range(3):
                x = n
                for j in range(3):
                    s[k-1].append(board[m][x])
                    x += 1
                m += 1
            n = (k*3)%9
            if k%3==0:
                n = 0
        for i in range(9):
            for j in range(9):
                # print((i//3)*3+j//3)
                if board[i][j] != '.' and (s[(i//3)*3+j//3].count(board[i][j]) > 1 or l[j].count(board[i][j]) > 1 or board[i].count(board[i][j]) > 1):
                    return 0
        return 1