# https://atcoder.jp/contests/abc012/tasks/abc012_4
# 全てのバス停に向かう上で、最大乗車時間が一番短い地点の最大乗車時間を出力する。
# indexが0から始まる仕様なので、便宜上バス停1を0, バス停2を1といったように表現する。
import heapq
input_file = open("bus_ride.txt")


def solution_by_dijkstra(start):

    cost_list = [float('inf') for _ in range(n)] #startからの各バス停への距離を格納するリスト
    cost_list[start] = 0 #スタート地点は0

    hq = [(0, start)]
    #ヒープの初期値はスタート地点がstart、かかる距離が0としておく
    heapq.heapify(hq)

    while hq:
        #調査対象のバス停をtarget, 前回のループでのtargetからそこまでいく距離をcostとする
        cost, target = heapq.heappop(hq)

        if cost > cost_list[target]:
            continue
        for d,g in routes[target]:
            #向かうバス停をg、gまでの距離をdとする
            tmp = cost + d
            if tmp < cost_list[g]:
                cost_list[g] = tmp
                heapq.heappush(hq, (tmp, g)) #次の調査対象はg、startからgまでの距離をtmpとしておく。
    return cost_list

    

while True:
    n,m = map(int,input_file.readline().split())

    if n == 0:
        break

    routes = [[] for _ in range(n)] # リスト内包表記でバス停の数だけリストを作る。そのリストの中に各バス停の路線を格納。
    distance_list = [] #各バス停から一番遠いバス停の距離を格納するリスト

    for _ in range(m):
        #a地点・b地点・ab間の距離
        a,b,t = map(int,input_file.readline().split())
        #バス停が1から始まるのに対し、indexは0から始まることに注意
        routes[a-1].append((t,b-1))
        routes[b-1].append((t,a-1))

    for i in range(n):
        distance = solution_by_dijkstra(i)
        max_dis = max(distance)
        distance_list.append(max_dis)

    print(min(distance_list))
