# https://codingcompetitions.withgoogle.com/codejam/round/0000000000432cc4/0000000000432bd8
input_file = open("watersheds.txt")


def node_connected_component(G, s):
    # sの連結成分をvisited_nodesに格納する。
    # print(visited)
    visited_nodes = set([s])
    boundary_nodes = set([s])
    
    # boundary_nodesという未踏の頂点を一時的に格納する辞書を用意しておければ、再帰的な関数にする必要はない
    while len(boundary_nodes) > 0:
        print(visited_nodes, boundary_nodes)
        v = boundary_nodes.pop()
        for w in G[v]:
            if w not in visited_nodes:
                visited_nodes |= set([w]) # .add(w)でもテストケースを通過できるが、ビット論理和代入の方が良さげ？
                boundary_nodes |= set([w])
    return visited_nodes
    
    #{(0, 0): [(1, 0)], 
    # (0, 1): [(0, 2)], 
    # (0, 2): [(0, 1), (1, 2)], 
    # (1, 0): [(0, 0), (2, 0), (1, 1)], 
    # (1, 1): [(1, 0)], 
    # (1, 2): [(0, 2)], 
    # (2, 0): [(1, 0), (2, 1)], 
    # (2, 1): [(2, 0), (2, 2)], 
    # (2, 2): [(2, 1)]}

    #case1でh=0,w=0の時に{(2, 1), (0, 0), (1, 1), (2, 0), (2, 2), (1, 0)}が出せればOK


def solution(H, W, altitude):
    G = {(h, w): [] for h in range(H) for w in range(W)} # 頂点名をキー，
    # 隣接する頂点のリストを値とする辞書で無向グラフを表す．
    for h in range(H):
        for w in range(W):
            altitude_of_lowest_neighbor = altitude[h][w]
            if h > 0 and altitude[h - 1][w] < altitude_of_lowest_neighbor:
                altitude_of_lowest_neighbor = altitude[h - 1][w]
                neighbor = (h - 1, w)
            if w > 0 and altitude[h][w - 1] < altitude_of_lowest_neighbor:
                altitude_of_lowest_neighbor = altitude[h][w - 1]
                neighbor = (h, w - 1)
            if w < W - 1 and altitude[h][w + 1] < altitude_of_lowest_neighbor:
                altitude_of_lowest_neighbor = altitude[h][w + 1]
                neighbor = (h, w + 1)
            if h < H - 1 and altitude[h + 1][w] < altitude_of_lowest_neighbor:
                altitude_of_lowest_neighbor = altitude[h + 1][w]
                neighbor = (h + 1, w)
            if altitude_of_lowest_neighbor < altitude[h][w]: # ここまでで隣接する区画の高さが自分の区画よりも真に小さいならば，
                G[(h, w)].append(neighbor) # その一番低い区画を自分の隣接頂点に加え，
                G[neighbor].append((h, w)) # 同時に，自分を，その一番低い区画の隣接頂点に加える．
    unicode_point = ord('a')
    sol = [['' for w in range(W)] for h in range(H)]
    for h in range(H):
        for w in range(W):
            if sol[h][w] != '':
                continue
            comp = node_connected_component(G, (h, w)) # ここでは，上記の自作の関数で連結成分（の頂点集合）を得る．
            for hh, ww in comp:
                sol[hh][ww] = chr(unicode_point)
            unicode_point += 1
    return sol


T = int(input_file.readline()) # Tをテストケースの数とする．
for case_number in range(1, T + 1): # テストケース1からTまで繰り返す．
    H, W = map(int, input_file.readline().split()) # HとWを行数と列数とする．
    altitude = [] # altitudeにそれぞれの区画の高さを保存するつもり．
    for h in range(H):
        row = list(map(int, input_file.readline().split()))
        altitude.append(row)
    sol = solution(H, W, altitude) # solution_with_nxで得られた，それぞれのテストケースの解をsolとする．
    print(f'Case #{case_number}:')
    for h in range(H): # 得られた解を，行ごとに，
        print(' '.join(sol[h])) # 空白を挟んで1つの文字列にして表示する．