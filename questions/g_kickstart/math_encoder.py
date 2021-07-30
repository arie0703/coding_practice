# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201d27/0000000000201b7b
# 現時点ではlarge testsetでTLEになるので改善が必要

import itertools

T = int(input())
    
for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    idx_list = [i for i in range(N)] #インデックスのリストを作る
    ans = 0
    for c in itertools.combinations(idx_list, 2):
        l = list(c)
        large, small = l[1], l[0]
        idx = 2 ** (large - small - 1)
        num = (arr[large] - arr[small]) * idx
        ans += num
    print(f'Case #{t + 1}:', ans)

    '''
    インデックスの部分集合の組み合わせをcombinationsで出す
    二つのインデックスからarrの中身を参照。
    インデックスの差 - 1　を2に乗じた数をarrの大きい数字から小さい数字を引いた数に掛ける
    '''




        

