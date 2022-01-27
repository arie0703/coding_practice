# 左上のマスから右下のマスまでの最短距離を求める

# greedy法を使います
def minPathSum(grid):
    col, row = len(grid), len(grid[0])
    # total = row * col
    # d = {i : 999 for i in range(1, total + 1)}
    # この方法だとTLEになる
    """
    def search(i, j, k):
        key = (j + 1) + (row * i)
        

        if grid[i][j] + k < d[key]:
            d[key] = grid[i][j] + k

            #最短距離が更新された時のみ、次のマスに進む計算を行う
            if i < col - 1:
                search(i + 1, j, d[key])
            if j < row - 1:
                search(i, j + 1, d[key])
    """

    
    # search(0, 0, 0)

    # gridを書き換える式でやると早い

    for i in range(col):
        for j in range(row):
            if i > 0 and j > 0:
                grid[i][j] = grid[i][j] + min(grid[i - 1][j], grid[i][j - 1])
            elif i == 0 and j > 0:
                grid[i][j] += grid[i][j - 1]
            elif j == 0 and i > 0:
                grid[i][j] += grid[i - 1][j]
    print(grid)
    return grid[col-1][row-1]


print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))

    

