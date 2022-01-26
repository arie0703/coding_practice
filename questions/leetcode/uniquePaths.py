import math 


# https://leetcode.com/problems/unique-paths-ii/discuss/1719038/Python-or-1D-DP

def uniquePathsWithObstacles(obstacleGrid):
    # 各地点にたどり着く組合せ数を調べることが可能
    comb = []

    if obstacleGrid[0][0] == 1:
        return 0
    
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    prev = [1] + [0]*(n-1)

    # 最初の一列目
    for j in range(1, n):
        if obstacleGrid[0][j] == 0:
            prev[j] = prev[j-1] 
        else:
            prev[j] = 0

    comb.append(prev)
    for i in range(1, m):
        cur = [0]*n

        # 2行目以降の横列を調査
        for j in range(n):
            if obstacleGrid[i][j] == 1:
                cur[j] = 0
            elif j == 0:
                cur[j] = prev[j]
            else:
                cur[j] = prev[j] + cur[j-1]
        comb.append(cur)
        prev = cur


    print(comb)
    return prev[-1]
    

# obstacleが一つの場合
def uniquePathsWithObstacle(obstacleGrid):

    # get obstacle index
    obstacle_idx = []
    for i, row in enumerate(obstacleGrid):
        if 1 in row:
            obstacle_idx = [i, row.index(1)]

    print(obstacle_idx)

    
    # get shortest path from start to goal
    m, n = len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1

    shortest_path = math.factorial(m + n) // (math.factorial(m) * math.factorial(n))
    # print(shortest_path)

    # if there are no obstacle, return shortest path
    if not obstacle_idx:
        return shortest_path

    # get shortest path from start to obstacle
    to_obstacle = math.factorial(obstacle_idx[0] + obstacle_idx[1]) // (math.factorial(obstacle_idx[0]) * math.factorial(obstacle_idx[1]))
    # print(to_obstacle)
            
    # get shortest path from obstacle to goal
    col, row = m - obstacle_idx[0], n - obstacle_idx[1]
    to_goal = math.factorial(col + row) // (math.factorial(col) * math.factorial(row))
    # print(to_goal)

    return shortest_path - (to_obstacle * to_goal)

print(uniquePathsWithObstacles([[0,0,1],[1,1,0],[0,0,0]]))
