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
            
            