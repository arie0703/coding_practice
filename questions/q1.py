#https://icpc.iisf.or.jp/past-icpc/domestic2007/A_ja.html

import math

l = [3, 1000, 342, 0, 5, 2, 2, 9, 11, 932, 5, 300, 1000, 0, 200, 400, 8, 353, 242, 402, 274, 283, 132, 402, 523, 0]

while len(l) > 1:
    # 審判の数
    n = l[0]
    #点数を格納するリスト
    score_list = []

    #リストの中に0だけが残ったらループ終了
    if n == 0:
        break

    for i in range(1, n + 1):
        #print(l[i])
        score_list.append(l[i])

    #スコアの最小値と最大値を除外
    score_list.remove(max(score_list))
    score_list.remove(min(score_list))

    #平均をとる
    score = math.floor(sum(score_list) / len(score_list))

    print(score)

    #スコア算出に使用した点数、及び審判の数を表す値をlistから削除、ループの最初に戻る。
    del l[:n + 1]
    

