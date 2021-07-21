#https://codingcompetitions.withgoogle.com/kickstart/round/0000000000434b3e/0000000000434adb

input_file = open("c.txt")

def solution(G, m):


    q = [i for i in range(1, m + 1)]
    # print(q)

    node = {}
    for i in range(m):
        node[i+1] = 0

    # 初期値を設定
    source = 1
    target = 1
    num = 1 #移動可能な部屋の数

    room_number = 0
    number_of_room = 0

    while q:
        v = q.pop(0)
        # print(v, source, target, num, max(node.values()))

        if G[source] == 0 or G[target] == 0:
            if num > max(node.values()): ##ループ回数が今までで最大だったら
                room_number = source #部屋番号と
                number_of_room = num #その部屋番号から移動できる部屋の数を更新。
            node[source] = num
            source = source + 1
            target = source
            num = 1
            continue
        else:
            num += 1
            target += 1
            q.insert(0, v)

    return [room_number, number_of_room]
        

    

while True:
    n = int(input_file.readline())

    for i in range(n):
        h = int(input_file.readline())
        arr = []
        
        for _ in range(h):
            arr.append(list(map(int, input_file.readline().split())))
        
        # print(arr)

        if n - i != 1:
            for _ in range(h):
                a = input_file.readline()
                # print("空白処理")

        G = {}
        for i in range(h):
            for j in range(h):
                G[arr[i][j]] = 0 #隣接頂点の初期化

        for i in range(h):
            for j in range(h):
                t = arr[i][j] + 1 #特定のマス目より１大きい数字を探す
                if i + 1 < h: #下から1段目ではない
                    if arr[i + 1][j] == t: #下のマス目
                        G[arr[i][j]] = arr[i + 1][j]
                if i != 0: #一番上の段ではない。
                    if arr[i - 1][j] == t:
                        G[arr[i][j]] = arr[i - 1][j]
                if j + 1 < h: #一番右ではない
                    if arr[i][j + 1] == t:
                        G[arr[i][j]] = arr[i][j + 1]
                if j != 0: #一番左ではない
                    if arr[i][j - 1] == t:
                        G[arr[i][j]] = arr[i][j - 1]
        #print(G)

        

        ans = solution(G, h**2)

        print(ans[0], ans[1])
        



    #loopおしまい
    break        
    