def solveNQueens(n):
    board = []
    res = []

    def isPossible(i, j):
        if i == 0:
            return True

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

        diagonal = [leftup(i,j),rightup(i,j)]
        if False in diagonal:
            return False
        return True
  

    
    def setQueen(i):

        if i == n:
            # そのままboardをresにappendすると、空のboardが追加されたことになってしまう。
            # 新しい変数にループでappendするか、deepcopyを使う。
            arr = []
            for b in board:
                arr.append(b)
            res.append(arr)
            return

        for j in range(n):
            if isPossible(i,j):
                board.append("." * j + "Q" + "." * (n - j - 1))
                setQueen(i + 1)
                board.pop()
        # クイーンが置けなかった場合、再帰が発生せずそのままnoneが返されて終わる。
    
    setQueen(0)
            
    return res
    
print(solveNQueens(4))