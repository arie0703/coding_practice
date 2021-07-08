#https://icpc.iisf.or.jp/past-icpc/domestic2009/all_ja.htm B問題

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
    remaining_nodes = set(G.keys()) # まだ吟味していない頂点の集合をGの頂点集合そのものとする．
    # 辞書のメソッドkeys()ですべてのキーが得られる．そしてこの場合，それがグラフの頂点集合になっている．
    # 実はnumber_connected_componentsと異なるのはここだけである．
    num = 0
    while len(remaining_nodes) > 0:
        v = remaining_nodes.pop()
        num += 1
        visited_nodes = set(graph_scanning_dict(G, v))
        scanned_nodes |= visited_nodes
        remaining_nodes -= visited_nodes
    return num

def answer_without_networkx():
    input_file = open("search_island.txt")
    while True:
        w, h = map(int, input_file.readline().split())
        if w == 0 and h == 0:
            break
        c = []
        for i in range(h):
            c.append(list(map(int, input_file.readline().split())))
        G = {} # 空の辞書だが，これは空の頂点隣接リストというつもりである．
        for i in range(h):
            for j in range(w):
                if c[i][j] == 1:
                    G[(i, j)] = [] # それぞれの頂点の，隣接頂点を空リストで初期化する
        for i in range(h):
            for j in range(w):
                if j < w - 1 and c[i][j] == 1 and c[i][j + 1] == 1:
                    G[(i, j)].append((i, j + 1)) # 頂点(i, j)の隣接頂点として(i, j + 1)を追加
                    G[(i, j + 1)].append((i, j)) # と同時に，頂点(i, j + 1)の隣接頂点として(i, j)を追加することを忘れない．
                if i < h - 1 and c[i][j] == 1 and c[i + 1][j] == 1:
                    G[(i, j)].append((i + 1, j))
                    G[(i + 1, j)].append((i, j))
                if i < h - 1 and j > 0 and c[i][j] == 1 and c[i + 1][j - 1] == 1:
                    G[(i, j)].append((i + 1, j - 1))
                    G[(i + 1, j - 1)].append((i, j))
                if i < h - 1 and j < w - 1 and c[i][j] == 1 and c[i + 1][j + 1] == 1:
                    G[(i, j)].append((i + 1, j + 1))
                    G[(i + 1, j + 1)].append((i, j))
        print(f'{number_connected_components_dict(G)}') # 完全自作のnumber_connected_components_dictを利用する．

answer_without_networkx()