# https://atcoder.jp/contests/abc207/tasks/abc207_b
def answer(a,b,c,d):
    blue = a
    red = 0
    n = 0

    #青玉の数が赤玉のd倍以下になればnを出力する
    while blue > red * d:
        n += 1
        blue += b
        red += c
        if n > 1 and b >= c * d: #一回に追加する青玉の数が赤玉のd倍だと無限ループになるので-1を出力
            return -1

    
    return n
        
a, b, c, d = map(int, input().split())
print(answer(a,b,c,d))


