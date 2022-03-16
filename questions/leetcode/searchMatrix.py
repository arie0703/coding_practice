def searchMatrix(matrix, target):
    for m in matrix:
        if m[-1] >= target and m[0] <= target:
            return True if target in m else False
        else:
            continue
    return False

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13))