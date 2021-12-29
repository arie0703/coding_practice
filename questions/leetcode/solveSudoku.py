# faster than 5% 結構遅い
# ハッシュマップ使うと速い？

def solveSudoku(board):

    def getNextCell():
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    return i,j
        return -1,-1

    def isValid(col, row, val):

        isRow = val not in board[col]
        isCol = val not in [b[row] for b in board]
        subRow, subCol = row // 3 * 3, col // 3 * 3

        subBlock = [v[subRow:subRow + 3] for v in board[subCol:subCol + 3]]
        isBlock = val not in sum(subBlock, [])


        return all([isRow, isCol, isBlock])

    def solve(col, row):
        col, row = getNextCell()

        if col == -1 and row == -1:
            return True

        for val in range(1,10):
            val = str(val)


            if isValid(col, row, val):
                board[col][row] = val
                
                # 現在のセルにvalを入れた状態で再帰させる
                if solve(col,val):
                    return True

                #現在のvalを入れた状態で解けなかったら、次回以降のループで別の値を入れる
                board[col][row] = "."

        return False

    solve(0,0)
    return board


board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

print(solveSudoku(board))
