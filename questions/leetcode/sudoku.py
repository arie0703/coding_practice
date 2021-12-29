


def isValidSudoku(board):

    def scan(c_s, c_e, r_s, r_e):
        print(c_s, c_e, r_s, r_e)
        if c_e - c_s == 3:
            print("sub boxの調査")
        elif c_e == 9 and c_s == 0:
            print(r_s + 1, "列目の調査")
        else:
            print(c_s + 1,  "行目の調査")
        nums = []
        for i in range(c_s, c_e):
            for j in range(r_s, r_e):

                print(board[i][j], nums)
                if board[i][j] != ".":
                    if int(board[i][j]) in nums:
                        print(False)
                        return False
                    else:
                        nums.append(int(board[i][j]))
        print("-----------------------------")
        return True


    for i in range(0, 9):
        isColumnValid = scan(0, 9, i, i + 1)
        isRowValid = scan(i, i + 1, 0, 9)

        if not isRowValid or not isColumnValid:
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not scan(i, i + 3, j, j + 3):
                return False
    
    return True


board = [[".",".",".","9",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".","3",".",".",".",".",".","1"],[".",".",".",".",".",".",".",".","."],["1",".",".",".",".",".","3",".","."],[".",".",".",".","2",".","6",".","."],[".","9",".",".",".",".",".","7","."],[".",".",".",".",".",".",".",".","."],["8",".",".","8",".",".",".",".","."]]

print(isValidSudoku(board))

