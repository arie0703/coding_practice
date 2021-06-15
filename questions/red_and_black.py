def graph_scanning_dict(G, s): # ここでGは頂点隣接リストの辞書表現である．
    visited_nodes = set([s])
    boundary_nodes = set([s])
    while len(boundary_nodes) > 0:
        v = boundary_nodes.pop()
        #指定した頂点と繋がっているタイルを探し、重複がないようにvisited_nodesに格納
        for w in G[v]:
            if w not in visited_nodes:
                visited_nodes |= set([w])
                boundary_nodes |= set([w])
    return visited_nodes


def number_connected_components_dict(G, x, y):
    remaining_nodes = set(G.keys()) # まだ吟味していない頂点の集合をGの頂点集合そのものとする．
    num = 0
    while len(remaining_nodes) > 0:
        v = remaining_nodes.pop() #頂点の集合から一つ頂点を取る
        visited_nodes = set(graph_scanning_dict(G, v))
        for i in range(len(visited_nodes)): # visited_nodesに"@"の座標が含まれていた場合、visited_nodesの要素数が到達できるタイルの数である。
            if list(visited_nodes)[i] == (x, y):
                num = len(visited_nodes)
                return num
        remaining_nodes -= visited_nodes
    return num


def answer():
    input_file = open("red_and_black.txt")
    while True:
        w, h = map(int, input_file.readline().split()) #最初に入力される幅と高さ
        # "@"が位置する座標を(x, y)とする
        x = 0
        y = 0
        if w == 0 and h == 0:
            break
        c = []
        for i in range(h): #入力された高さの分だけ0と1の座標が与えられる
            c.append(list(map(str, input_file.readline().replace("\n", ""))))
        G = {}
        for i in range(h):
            for j in range(w):
                if c[i][j] == "." or c[i][j] == "@":
                    G[(i, j)] = [] # それぞれの頂点の，隣接頂点を空リストで初期化する
                    if c[i][j] == "@":
                        x, y = i, j
        for i in range(h):
            for j in range(w):
                if j < w - 1 and c[i][j] == "." and c[i][j + 1] == ".":
                    G[(i, j)].append((i, j + 1))
                    G[(i, j + 1)].append((i, j))
                if j < w - 1 and c[i][j] == "@" and c[i][j + 1] == ".":
                    G[(i, j)].append((i, j + 1))
                    G[(i, j + 1)].append((i, j))
                if j < w - 1 and c[i][j] == "." and c[i][j + 1] == "@":
                    G[(i, j)].append((i, j + 1))
                    G[(i, j + 1)].append((i, j))
                if i < h - 1 and c[i][j] == "." and c[i + 1][j] == ".":
                    G[(i, j)].append((i + 1, j))
                    G[(i + 1, j)].append((i, j))
                if i < h - 1 and c[i][j] == "@" and c[i + 1][j] == ".":
                    G[(i, j)].append((i + 1, j))
                    G[(i + 1, j)].append((i, j))
                if i < h - 1 and c[i][j] == "." and c[i + 1][j] == "@":
                    G[(i, j)].append((i + 1, j))
                    G[(i + 1, j)].append((i, j))
        print(number_connected_components_dict(G, x, y))
    input_file.close()
    return

answer()