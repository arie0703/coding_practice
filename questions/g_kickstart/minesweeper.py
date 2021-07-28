# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000434d9f/0000000000434c0c

#0と隣接しているセルは同時に開示される。

def graph_scanning_dict(G, s): # ここでGは頂点隣接リストの辞書表現である．
    visited_nodes = set([s])
    boundary_nodes = set([s])
    while len(boundary_nodes) > 0:
        v = boundary_nodes.pop()
        for w in G[v]: # graph_scanningと異なるのは，ここだけである．
            if w not in visited_nodes:
                visited_nodes |= set([w])
                boundary_nodes |= set([w])
    return visited_nodes


def number_connected_components_dict(G): # ここでもGは頂点隣接リストの辞書表現である．
    scanned_nodes = set([])
    remaining_nodes = set(G.keys()) # 
    num = 0
    while len(remaining_nodes) > 0:
        v = remaining_nodes.pop()
        num += 1
        visited_nodes = set(graph_scanning_dict(G, v))
        scanned_nodes |= visited_nodes
        remaining_nodes -= visited_nodes
    return num





T = int(input())

for t in range(T):
    N = int(input())

    arr = []
    for i in range(N):
        arr.append(list(map(str, input())))

    #print(arr)
    #地雷が埋まっているマスと幾つ隣接しているかのリスト
    #地雷があるところは*を挿入しておく
    G = {}
    revealed = [[0] * N for i in range(N)]
    '''
    注意：２次元配列を生成するとき、リスト内包表記にしないと代入がうまくいかなくなる
    [[0] * N] * Nだとうまくいかない
    参考：　https://qiita.com/oyoshi0022/items/7475951f465d20ad4970
    '''
    for i in range(N):
        for j in range(N): 
            if arr[i][j] == "*":
                revealed[i][j] = -1
            else:
                G[(i, j)] = []

    

    # print(arr)

    
    

    # 地雷が埋まってるマスに関しては隣接リストを作らなくて良い
    for i in range(N):
        for j in range(N):
            if revealed[i][j] == -1:
                if j < N - 1:
                    if arr[i][j + 1] == ".":
                        G[(i, j + 1)].append((i, j))
                    if i < N - 1 and arr[i + 1][j + 1] == ".": #一番下じゃない
                        G[(i + 1, j + 1)].append((i, j))
                    if i < N - 1 and arr[i + 1][j] == ".":
                        G[(i + 1, j)].append((i, j))
                    if j > 0 and i < N - 1 and arr[i + 1][j - 1] == ".":
                        G[(i + 1, j - 1)].append((i, j))
                else: # 右端の場合
                    if i < N - 1 and arr[i + 1][j] == ".":
                        G[(i + 1, j)].append((i, j))
                    if i < N - 1 and arr[i + 1][j - 1] == ".":
                        G[(i + 1, j - 1)].append((i, j))
            else:
                # 左端のマスなら右、下、斜め右下、右端なら下、斜め左下
                if j < N - 1: #右端じゃない場合
                    if arr[i][j + 1] == "*": 
                        G[(i, j)].append((i, j + 1))
                    if i < N - 1 and arr[i + 1][j + 1] == "*": #一番下じゃない&右斜め下
                        G[(i, j)].append((i + 1, j + 1))
                    if  i < N - 1 and arr[i + 1][j] == "*": # 一番下じゃない
                        G[(i, j)].append((i + 1, j))
                    if j > 0 and i < N - 1 and arr[i + 1][j - 1] == "*":
                        G[(i, j)].append((i + 1, j - 1))
                else: # 右端の場合
                    if i < N - 1 and arr[i + 1][j] == "*":
                        G[(i, j)].append((i + 1, j))
                    if i < N - 1 and arr[i + 1][j - 1] == "*":
                        G[(i, j)].append((i + 1, j - 1))


    
    
    for i in range(N):
        for j in range(N):
            if revealed[i][j] > -1:
                revealed[i][j] = len(G[(i , j)])

    R = {}

    for i in range(N):
        for j in range(N): 
            if revealed[i][j] > -1:
                R[(i, j)] = []
    
    # print(revealed)
    for i in range(N):
        for j in range(N):
            if revealed[i][j] > 0:
                if len(R[(i, j)]) > 0:
                    continue
                if j < N - 1 and revealed[i][j + 1] == 0 and len(R[(i, j)]) < 1: # 右
                    R[(i, j)].append((i, j + 1))
                    R[(i, j + 1)].append((i, j))
                if i < N - 1 and revealed[i + 1][j] == 0 and len(R[(i, j)]) < 1: #下
                    R[(i, j)].append((i + 1, j))
                    R[(i + 1, j)].append((i, j))
                if j > 0 and i < N - 1 and revealed[i + 1][j - 1] == 0 and len(R[(i, j)]) < 1:
                    R[(i, j)].append((i + 1, j - 1))
                    R[(i + 1, j - 1)].append((i, j))
                if j < N - 1 and i < N - 1 and revealed[i + 1][j + 1] == 0 and len(R[(i, j)]) < 1:
                    R[(i, j)].append((i + 1, j + 1))
                    R[(i + 1, j + 1)].append((i, j))
            elif revealed[i][j] == 0:
                if j < N - 1 and revealed[i][j + 1] == 0: # 右
                    R[(i, j)].append((i, j + 1))
                    R[(i, j + 1)].append((i, j))
                if i < N - 1 and revealed[i + 1][j] == 0: #下
                    R[(i, j)].append((i + 1, j))
                    R[(i + 1, j)].append((i, j))
                if j > 0 and i < N - 1 and revealed[i + 1][j - 1] == 0: #左下
                    R[(i, j)].append((i + 1, j - 1))
                    R[(i + 1, j - 1)].append((i, j))
                if j < N - 1 and i < N - 1 and revealed[i + 1][j + 1] == 0: #右下
                    R[(i, j)].append((i + 1, j + 1))
                    R[(i + 1, j + 1)].append((i, j))
                if j < N - 1 and revealed[i][j + 1] > 0 and len(R[(i, j + 1)]) < 1: # 右
                    R[(i, j)].append((i, j + 1))
                    R[(i, j + 1)].append((i, j))
                if i < N - 1 and revealed[i + 1][j] > 0 and len(R[(i + 1, j)]) < 1: #下
                    R[(i, j)].append((i + 1, j))
                    R[(i + 1, j)].append((i, j))
                if j > 0 and i < N - 1 and revealed[i + 1][j - 1] > 0 and len(R[(i + 1, j - 1)]) < 1: #左下
                    R[(i, j)].append((i + 1, j - 1))
                    R[(i + 1, j - 1)].append((i, j))
                if j < N - 1 and i < N - 1 and revealed[i + 1][j + 1] > 0 and len(R[(i + 1, j + 1)]) < 1: #右下
                    R[(i, j)].append((i + 1, j + 1))
                    R[(i + 1, j + 1)].append((i, j))
    print(f'Case #{t + 1}:', number_connected_components_dict(R))




    
        
                
'''
例外パターン
001*
0011
1100
*100

0同時が斜めで隣り合う時はつなげない


'''

                    


            
            
            

'''
02*20
13*31
2*32*
3*311
2*200

*..*211**1
1112*22221
00012*1111
00001111*1
0000000111
'''