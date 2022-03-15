def setZeroes(matrix):
    col = len(matrix)
    row = len(matrix[0])

    # 0が存在する行・列のindexを格納するリスト
    idx_col = []
    idx_row = []

    for i in range(col):
        for j in range(row):
            if matrix[i][j] == 0:
                if not i in idx_col:
                    idx_col.append(i)
                if not j in idx_row:
                    idx_row.append(j)

    print(idx_col, idx_row)
    for c in idx_col:
        matrix[c] = [0 for _ in range(row)]

    for r in idx_row:
        for i in range(col):
            matrix[i][r] = 0

    return matrix

print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
