#問題 2**a * 3**b * 5**cの形の正整数を小さい順にN個列挙せよ。
#参考記事 https://qiita.com/convexineq/items/aca8dde73cc866aa362a

from collections import deque
n = 16 #ここではnを16とする
res = [1]*n #resにn個のリストを作り、1という数字をあらかじめ入れておく
q = [deque(),deque(),deque()]
min_values = [2,3,5]

for i in range(1,n):
    
    res[i] = v = min(min_values) #vに最小数を代入
    idx = min_values.index(v)  #min_valuesの中で最小値があるインデックスを取得

    q[0].append(2*v)
    #q[0]は2,q[1]は3,q[2]は5に対応する数を格納している
    #最小値vがq[0]から取り出された場合、q[0]に2xを格納
    #q[1]から取り出された場合、q[0]に2x、q[1]に3xを格納
    #q[2]から取り出された場合、q[0]に2x、q[1]に3x、q[2]に5xを格納

    #q[0]には2**n, 3**n, 5**nの乗数が格納されている。
    #一方でq[1]には2**0, 3**n, 5**nの乗数が格納。
    if idx >= 1:
        q[1].append(3*v)
    if idx >= 2:
        q[2].append(5*v)
    

    min_values[idx] = q[idx].popleft()

print(res) #[1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25]
