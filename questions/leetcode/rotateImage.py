def rotate(matrix):
    l = len(matrix)
    for i in range(l // 2 + l % 2):
        for j in range(l // 2):
            
            """
            5x5のマスで4隅を左上・右上・右下・左下の順に1,5,25,21とする
            この四つの位置を21,1,5,25としたい場合、tempに左上の数字を入れていき、
            左上から反時計回りに数字を更新する
            最後に右上の数字をtempに入れておいた元々の左上の値（matrix[i][j]）を入れる。
            """
            temp = matrix[i][j]
            matrix[i][j] = matrix[l - 1 - j][i]
            matrix[l - 1 - j][i] = matrix[l - 1 - i][l - 1 - j]
            matrix[l - 1 - i][l - 1 - j] = matrix[j][l - 1 - i]
            matrix[j][l - 1 - i] = temp

            # print(matrix[i][j], matrix[j][l - 1 - i], matrix[l - 1 - i][l - 1 - j], matrix[l - 1 - j][i])
    print(matrix)

    return 

lis = [[i for i in range(j * 5 + 1, j * 5 + 6)] for j in range(5)]
for l in lis:
    print(l)
m = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(rotate(m))