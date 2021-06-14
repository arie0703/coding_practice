import networkx as nx

def answer():
    input_file = open("search_island.txt")
    while True:
        w, h = map(int, input_file.readline().split()) #最初に入力される幅と高さ
        if w == 0 and h == 0:
            break
        c = []
        for i in range(h): #入力された高さの分だけ0と1の座標が与えられる
            c.append(list(map(int, input_file.readline().split())))
        G = nx.Graph()
        for i in range(h):
            for j in range(w):
                if c[i][j] == 1:
                    G.add_node((i, j))
                if j < w - 1 and c[i][j] == 1 and c[i][j + 1] == 1:
                    G.add_edge((i, j), (i, j + 1))
                if i < h - 1 and c[i][j] == 1 and c[i + 1][j] == 1:
                    G.add_edge((i, j), (i + 1, j))
                if i < h - 1 and j > 0 and c[i][j] == 1 and c[i + 1][j - 1] == 1:
                    G.add_edge((i, j), (i + 1, j - 1))
                if i < h - 1 and j < w - 1 and c[i][j] == 1 and c[i + 1][j + 1] == 1:
                    G.add_edge((i, j), (i + 1, j + 1))
        print(nx.number_connected_components(G))
    input_file.close()
    return

answer()