from collections import deque #pop処理を高速化するためdequeを使用する

def solution(G, m, source, target):
    q = deque([i for i in range(1, m + 1)]) #dequeに1からm（部屋の数）までの数字を格納
    node = {} #各部屋の番号とそこから移動できる部屋番号のペアとなる辞書型リストを作る
    for i in range(m):
        node[i+1] = 0 #各部屋の初期値は0とする

    r = 0 #勝利する部屋番号
    d = 0 #移動できる部屋の数

    while q:
        v = q.popleft() #1から順に数字を取り出していく。（通常のpopを使うとTLEになるが、dequeのpopleftを使うと早い）
        if G[source] == 0 or G[target] == 0: #移動できる部屋がなかったら
            if target - source + 1 > max(node.values()): 
                r = source 
                d = target - source + 1
            if target - source > 0: #出発点から幾つか移動できる部屋があったら
                for _ in range(target - source): #それらの部屋をsourceとしてループを回す必要はないので(6から9まで行けた場合、7から出発したとしても最大移動回数にはならない)
                    q.popleft() #popleftで消してループ回数を少なく済ます。
            node[source] = target - source + 1 #nodeの出発地点の部屋番号に、そこから移動できる部屋の数を割り当てる
            source = target + 1 #出発点を更新
            target += 1 #吟味対象の部屋番号を更新
            continue
        else: #移動できる部屋があったら
            target += 1 #次の部屋へ進む
            q.appendleft(v)

    return [r, d]


n = int(input()) #テストケースの数を取得
for x in range(n):
    e = input()
    queue = deque([0])
    while queue: #テストケース入力の後の空白入力を処理する。
        b = queue.popleft()

        if e == '': #空白だったらdequeに0を加えてループを回す。数字が入力されるまで繰り返される。
            e = input()
            queue = deque([0])
        else:
            break
    h = int(e) #迷路の長さを取得

    arr = []  
    for _ in range(h): #arrに迷路を格納
        arr.append(list(map(int, input().split())))

    G = {} #各部屋番号から移動できる部屋を格納する辞書型リスト。
    for i in range(h):
        for j in range(h):
            G[arr[i][j]] = 0 #各部屋番号の初期値は0とする

    for i in range(h):
        for j in range(h):
            t = arr[i][j]

            if i + 1 < h: #迷路の一番下じゃない場合
                if arr[i + 1][j] == t + 1: #下の部屋番号がtより1大きい場合
                    G[t] = arr[i + 1][j] #G[t]にその部屋番号を格納
                elif arr[i + 1][j] == t - 1: #下の部屋番号がtより1小さい場合
                    G[arr[i + 1][j]] = t #G[下の部屋番号]にtの部屋番号を格納

            if j + 1 < h: #迷路の一番右じゃない場合
                if arr[i][j + 1] == t + 1: #右の部屋番号がtより1大きい場合
                    G[t] = arr[i][j + 1] #G[t]にその部屋番号を格納
                elif arr[i][j + 1] == t - 1: #右の部屋番号がtより1小さい場合
                    G[arr[i][j + 1]] = t #G[右の部屋番号]にその部屋番号を格納

    ans = solution(G, h**2, 1, 1) #solutionにGと部屋の数(hの二乗), 出発地となる部屋番号(source)、その部屋番号から移動できる部屋があるか調査対象となる部屋番号を渡す(target)
    r, d = ans[0], ans[1]
   
    print(f'Case #{x+1}:', r, d)