V = ['1', '2', '3', '4'] # 有向グラフの頂点集合をVとする．

E = [('1', '2'), ('1', '3'), ('2', '3'), ('2', '4'), ('3', '4')] # 有向グラフの枝集合をEとする．

length = { # それぞれの枝の長さも辞書で保存する．  
    ('1', '2'): 2, # ①から②への有向枝の長さは2である．
    ('1', '3'): 6,
    ('2', '3'): 1,
    ('2', '4'): 5,
    ('3', '4'): 3,
}
def dijkstra(V, # 有向グラフの頂点集合
             E, # 有向枝集合
             length, # 枝長さ
             source, # 始点
            ):

    successor = {v: [] for v in V}
    for tail, head in E:
        successor[tail] += head

    distance = {} # 最短路長distanceは辞書で出力することにする．
    upper_bound_of_shortest_path_length = sum(length.values())
    #最短路長の自明な上界として「枝長さの合計」を使うことにする．
    for v in V:
        distance[v] = upper_bound_of_shortest_path_length

    distance[source] = 0 # 始点そのものへの最短路長は0である．

    U = V[:] # 集合（リスト）Uに頂点集合をコピーする．

    while len(U) > 0:

        minimum_of_d = upper_bound_of_shortest_path_length
        v = U[0]
        for u in U:
            if distance[u] < minimum_of_d:
                v = u
                minimum_of_d = distance[v]

        U.remove(v)

        for w in successor[v]:
            if distance[w] > distance[v] + length[(v, w)]:
                distance[w] = distance[v] + length[(v, w)]

    return distance

def shortest_path_edges(V, E, length, source, distance):
    '''
    前準備として，頂点が与えられたらその頂点に入ってくる枝の元の頂点のリストを引ける辞書predecessorを作る．
    '''
    predecessor = {v: [] for v in V}
    for tail, head in E:
        predecessor[head] += [tail]
    
    '''
    distance(pred) + length[(pred, v)] = distance(v)
    となっている頂点対(pred, v)があったら，
    それは最短路で使われているはずである．
    '''
    edges = [] # 最短路で使われている枝を保存するリスト
    for v in V: # それぞれの頂点に関して以下を行う．
        if v == source: # vが始点ならば
            continue # なにもしない．
        for pred in predecessor[v]: # vに入ってくる枝（の元）それぞれに関して，
            if length[(pred, v)] == distance[v] - distance[pred]:
                # もしも最適性条件を満たしているならば，
                edges += [(pred, v)] # それは最短路で使われているはずである．
                break
    return edges

shortest_distance = dijkstra(V, E, length, '1') #1を起点に

print(shortest_distance)