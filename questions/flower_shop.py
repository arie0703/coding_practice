# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201ca2/0000000000201c09


def total_cash(M, C, r): #方程式
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

    while upper - lower > 0.0000000000001:
        i += 1
        
        if upper + lower == 0:
            middle = 0
        else:
            middle = (upper + lower) / 2

        
        if total_cash(M, C, middle) < 0:
            upper = middle
        elif total_cash(M, C, middle) > 0:
            lower = middle
        else:
            return round(middle, 12)
    return round(middle, 12)
    

def solution(M, C):
    return solve_by_binary_search(M, C, -1, 1)


input_file = open('flower_shop.txt')

for i in range(int(input_file.readline()) * 2):
    inp = list(map(int, input_file.readline().split(' ')))
    if len(inp) == 1:
        month = inp[0]
    else:
        cash = inp
        print(solution(month, cash))