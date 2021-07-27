#https://atcoder.jp/contests/typical90/tasks/typical90_j

N = int(input())
c = [0] * N # class
s = [0] * N # score
for i in range(N):
    c[i], s[i] = map(int, input().split())
 
Q = int(input())
start = [0] * Q
end = [0] * Q
# 学籍番号がstartからendまでの累積和を求める
for i in range(Q):
    start[i], end[i] = map(int, input().split())
 
# 1組、2組の累積和のリストを作る。
sum1 = [0] * (N + 1)
sum2 = [0] * (N + 1)
for i in range(N):
    sum1[i+1] = sum1[i]
    sum2[i+1] = sum2[i]    
    if c[i] == 1:
        sum1[i+1] += s[i]
    else:
        sum2[i+1] += s[i]
 

for i in range(Q):
    print(sum1[end[i]] - sum1[start[i]-1], sum2[end[i]] - sum2[start[i]-1])

'''
1組と2組の得点の累積和リストを作って、特定の2つの学籍番号の間の累積和を求める
大きい方の学籍番号までの累積和から、0から小さい方の学籍番号-1までの累積和を引いた数を出力すればOK
'''



# 以下のプログラムはTLEになってしまった・・
# スライスを使うと遅い？
'''
# N = int(input())

# l_class1 = [0] * N
# l_class2 = [0] * N
# for i in range(N):
#     c, s = map(int, input().split()) #クラスと得点を取得
#     if c == 1:
#         l_class1[i] = s
#     else:
#         l_class2[i] = s
    
# Q = int(input())

# for q in range(Q):
#     start, end  = list(map(int, input().split()))
#     print(sum(l_class1[start-1:end]),sum(l_class2[start-1:end]))
'''