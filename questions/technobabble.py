# https://codingcompetitions.withgoogle.com/codejam/round/0000000000201b6c/0000000000201d19
#
import networkx as nx

def solution_with_nx(N, topic):
    H = nx.DiGraph()
    for i in range(N):
        a, b = topic[i]
        H.add_edge('a'+a, 'b'+b, capacity=1)
    H.add_node('source')
    H.add_node('target')
    for i in range(N):
        a, b = topic[i]
        H.add_edge('source', 'a'+a, capacity=H.out_degree('a'+a)-1)
        H.add_edge('b'+b, 'target', capacity=H.in_degree('b'+b)-1)
    flow_value, flow_dict = nx.maximum_flow(H, 'source', 'target')
    return flow_value

def solution(N, topic):
    l = []
    already = []
    count = 0
    for t in topic:
        if t[0] in l and not t[0] in already:
            already.append(t[0])
        else:
            l.append(t[0])
        if t[1] in l and not t[1] in already:
            already.append(t[1])
        else:
            l.append(t[1])

    print(l, already)
    for i, j in topic:
        if i in already and j in already:
            #一つ目の単語・二つ目の単語が同時にalreadyにあればcount++
            count += 1

    return count

    




topic = [('HYDROCARBON', 'COMBUSTION'), ('QUAIL', 'BEHAVIOR'), ('QUAIL', 'COMBUSTION')]
#一つ目・二つ目の単語が他でも使われていたら偽物と判定
print(solution(len(topic), topic))

