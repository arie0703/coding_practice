def solveNQueens(n):
    res = []

    def isPossible(i, j):
        #横に他の駒がいないか
        if "Q" in board[i]:
            return False

        #縦に他の駒がいないか
        for b in board:
            if b[j] == "Q" :
                return False

        #斜めに他の駒がいないか 

        def leftup(i, j):
            if i == 0 or j == 0: 
                return True
            if board[i - 1][j - 1] == "Q":
                return False
            return leftup(i - 1, j - 1)


        def rightup(i, j):

            if i == 0 or j == n - 1: #右上
                return True
            if board[i - 1][j + 1] == "Q":
                return False
            return rightup(i - 1, j + 1)

        def leftdown(i, j):

            if i == n - 1 or j == 0: #左下
                return True
            if board[i + 1][j - 1] == "Q":
                return False
            return leftdown(i + 1, j - 1)

        def rightdown(i, j):
            if i == n - 1 or j == n - 1: #右下
                return True
            if board[i + 1][j + 1] == "Q":
                return False
            return rightdown(i + 1, j + 1)

        diagonal = [leftup(i,j),rightup(i,j),leftdown(i,j),rightdown(i,j)]
        if False in diagonal:
            return False
        return True
  

    def setQueen(i,s):

        if i == n:
            return 

        for j in range(s, n):
            if board[i][j] == "." and isPossible(i,j):
                board[i][j] = "Q"
                setQueen(i + 1, 0)


        #どこにもクイーンが置けなかったら
        if not "Q" in board[i]:

            s = board[i - 1].index("Q")
            if s < n - 1:
                board[i - 1][s] = "."
                setQueen(i - 1, s + 1)# 一つ上の行のQがある位置をスタートとし、Qを再配置する。

        
    for i in range(n):
        board = [["." for _ in range(n)] for _ in range(n)]
        board[0][i] = "Q"
        setQueen(1,0)


        arr = []
        for b in board:
            if not "Q" in b:
                break
            else:
                arr.append("".join(b))
            
        if len(arr) == n:
            res.append(arr)
                
            
    return res
    
#この方法だとn通りのパターンしか得られない。
print(solveNQueens(5))


# https://leetcode.com/problems/n-queens/discuss/243428/Python-solution
def betterSolution(n):
    def backtrack(i):
        if i == n:
            res.append(list(board))
        for j in range(n):
            if j not in cols and j-i not in diag and j+i not in off_diag:
                cols.add(j)
                diag.add(j-i)
                off_diag.add(j+i)
                board.append("."*(j)+"Q"+"."*(n-j-1))
                backtrack(i+1)
                board.pop()
                off_diag.remove(j+i)
                diag.remove(j-i)
                cols.remove(j)
    res = []
    board = []
    cols = set()
    diag = set()
    off_diag = set()
    backtrack(0)
    return res

print(betterSolution(5))