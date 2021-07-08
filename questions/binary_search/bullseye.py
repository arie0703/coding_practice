#https://codingcompetitions.withgoogle.com/codejam/round/0000000000432b32/0000000000432cd1

import math

def calculate(r, t):
    # pi = math.pi
    # paint = t * pi # 1mlで1piセンチ平方メートルカバーできる。 tmlで描けるリングの面積を表す変数
    # required_inks = 0 #黒リングのトータル面積
    # n = 0 #ループ回数・リングをかける最大回数

    # while paint > required_inks:
    #     #黒リングの半径はループ回数が一回増えるごとに2cmずつ増える
    #     r += 2 * n

    #     #ring = (r + 1) ** 2 * pi - r ** 2 * pi
    #     ring = (2 * r + 1) * pi
    #     required_inks += ring

    #     if required_inks > paint:
    #         break
    #     n += 1

    # print(n)

    #  m個の円を作るために、2 * (m ** 2) + (2 * r - 1) * mのペンキが必要
    m = (1 - 2 * r + math.sqrt((2 * r - 1) ** 2 + 8 * t)) // 4
    print(m)
    # この関数だと正確な数値が出ない

def is_possible (m, r, t):
    # 円をm本作れるならばTrue、作れないならFalseを返す
    if 2 * (m ** 2) + (2 * r  - 1) * m <= t:
        return True
    else: 
        return False

def calculate_by_binary_search(lower, upper, r, t):
    #r, tに加え、mの下界・上界を与える。
    while upper - lower > 1:
        middle = (upper + lower) // 2
        if is_possible(middle, r, t) == True:
            lower = middle
        else:
            upper = middle

    if is_possible(upper, r, t) == True:
        return upper
    else:
        return lower



input_file = open('bullseye.txt')

for i in range(int(input_file.readline())):
    output = input_file.readline().split(' ')
    r = int(output[0])
    t = int(output[1])
    print(calculate_by_binary_search(0, 1000000000000000000, r,t))



