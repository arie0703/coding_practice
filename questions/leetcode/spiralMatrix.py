def spiralOrder(matrix):
    order = []

    def reverseRow(matrix):
        for m in matrix:
            m.reverse()

    def popColumn(matrix, order):
        for m in matrix:
            print(m)
            order.append(m.pop())
        return

    def makeSpiral(matrix, order):

        if not matrix:
            return order

        order.extend(matrix[0])
        del matrix[0]

        
        if matrix and matrix[0]:
            popColumn(matrix, order)
        
        # 最下層の列を逆から回収する
        if matrix:
            lastrow = matrix.pop()
            lastrow.reverse()
            order.extend(lastrow)
        
        # 下から上へ
        if matrix and matrix[0]:
            matrix.reverse()
            reverseRow(matrix)
            popColumn(matrix, order)
            reverseRow(matrix)
            matrix.reverse()

            # また上から再帰
            makeSpiral(matrix, order)

        return order

    res = makeSpiral(matrix, order)

    return res
m = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(m))

"""
1  2  3  4  5
6  7  8  9  10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
"""

def generateMatrix(n):

    stack = []
    res = [[0 for _ in range(n)] for _ in range(n)]
    c = 0
    for i in range(n**2,0,-1):
        stack.append(i)

    while stack:

        # 右から左
        for i in range(c, c + n - 1):
            res[c][i] = stack.pop()

        # 上から下
        for i in range(c, c + n - 1):
            res[i][-c-1] = stack.pop()

        # 左から右
        for i in range(c + n - 1, c, -1):
            res[-c-1][i] = stack.pop()

        # 下から上
        for i in range(c + n - 1, c, -1):
            res[i][c] = stack.pop()

        if c == c + n - 1: # center
            res[c][c] = stack.pop()

        n -= 2
        c += 1

    return res

print(generateMatrix(3))

        
        



            
            