# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201ca2/0000000000201c09


def total_cash(M, C, r): #方程式 rが大きくなると数値が小さくなる。
    cash = 0
    rate = 1
    for i in range(M, 0, -1):
        cash += C[i] * rate
        rate *= 1 + r
    cash -= C[0] * rate
    return cash

def solve_by_binary_search(M, C, lower, upper): #total_cashの方程式の解が0になるようなrを求めるため、２分探索を利用
    middle = 0
    i = 0

    while upper - lower > 10 ** -10: #upper - lower > 0にしてしまうとcase2で永遠に計算が終わらないので、今回は10 ** -10としておく
        i += 1
        
        if upper + lower == 0:
            middle = 0
        else:
            middle = (upper + lower) / 2

        #total_cashの方程式のrにmiddleを代入する
        #そこで得られた数値が0よりも大きい場合、rをもっと大きい数値にするためlowerにmiddleを代入
        #0よりも小さい場合、rをもっと小さい数値にするためupperにmiddleを代入
        if total_cash(M, C, middle) < 0:
            upper = middle
        elif total_cash(M, C, middle) > 0:
            lower = middle
        else:
            return middle
    return middle
    

def solution(M, C):
    return solve_by_binary_search(M, C, -1, 1)


# input_file = open('flower_shop.txt')

# for i in range(int(input_file.readline()) * 2):
#     inp = list(map(int, input_file.readline().split(' ')))
#     if len(inp) == 1:
#         month = inp[0]
#     else:
#         cash = inp
#         print(solution(month, cash))

T = int(input())
for case_number in range(1, T + 1):
    M = int(input())
    C = list(map(int, input().split()))
    print(f'Case #{case_number}: {round(solution(M, C), 9)}') # 組み込み関数round(x, y)は値xを小数第y位までに丸めて（四捨五入して）返す関数である．
    # yのデフォルト値は0であり，yが0のときは整数への丸めを意味する．