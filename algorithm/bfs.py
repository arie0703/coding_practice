# 幅優先探索
# 各辺に重みがない場合に用いられる。

from collections import deque

def bfs_tree(tree):
    
    #rootの0は最初からdequeの0としておく
    queue = deque([0])
    while queue:
        now = queue.popleft()
        for i in tree[now]:
            queue.append(i)
    return now

# 木構造を定義
tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [], [], [], [], [], [], [], []]
print(bfs_tree(tree))