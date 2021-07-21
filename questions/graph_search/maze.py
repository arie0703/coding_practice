#https://icpc.iisf.or.jp/past-icpc/domestic2010/#section_B

def shortest_path_length_without_nx(G, source, target):
    '''グラフ上の距離（最短路長）を返す関数
    入力は，グラフG，始点source，終点target，
    出力は，始点から終点へのグラフ上の距離，ただし始点と終点が同じ連結成分に含まれていない場合には-1'''
    # 以降，前出の関数shortest_path_length_with_nxと同じコメントは省略する．
    C = set([source])
    queue = [source]
    print(queue)
    dist = {source: 0}
    while len(queue) > 0:
        v = queue.pop(0)
        for w in G[v]: # 違うのはここだけ！ここでGは頂点隣接リスト（の辞書による実現）であると仮定している．
            if w not in C:
                C |= set([w])
                queue.append(w)
                dist[w] = dist[v] + 1
    if target in C:
        return dist[target]
    return -1


def answer(input_file_name, output_file_name):
    with open(input_file_name) as input_file, open(output_file_name, 'w') as output_file:
        while True:
            w, h = map(int, input_file.readline().split())
            if w == 0 and h == 0:
                break
            G = {} # 頂点隣接リスト（の辞書による実現）をGとする．
            for i in range(h):
                for j in range(w):
                    G[(i, j)] = [] # まずは，それぞれの頂点(i, j)の隣接頂点のリストを空にする．
            for i in range(h):
                line = list(map(int, input_file.readline().split()))
                for j in range(w - 1):
                    if line[j] == 0: # 頂点(i, j)の右の壁がないならば，
                        G[(i, j)].append((i, j + 1)) # 頂点(i, j)の隣接頂点のリストに頂点(i, j + 1)を加え，
                        G[(i, j + 1)].append((i, j)) # 逆に，頂点(i, j + 1)の隣接頂点のリストに頂点(i, j)を加える．
                        # このようにエッジの両端点のリストを処理する必要がないという意味で，NetworkXは便利である．
                if i >= h - 1: continue
                line = list(map(int, input_file.readline().split()))
                for j in range(w):
                    if line[j] == 0:
                        G[(i, j)].append((i + 1, j)) # 頂点(i, j)の隣接頂点のリストに頂点(i + 1, j)を加え，
                        G[(i + 1, j)].append((i, j)) # 逆に，頂点(i + 1, j)の隣接頂点のリストに頂点(i, j)を加える．
            source = (0, 0)
            target = (h - 1, w - 1)
            output_file.write(f'{shortest_path_length_without_nx(G, source, target) + 1}\n') # NetworkXを使わない関数に変更した．
    return

print(answer("maze.txt", "maze_output.txt"))