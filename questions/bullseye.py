#https://codingcompetitions.withgoogle.com/codejam/round/0000000000432b32/0000000000432cd1

import math

def calculate(r, t):
    pi = math.pi
    paint = t * pi # 1mlで1piセンチ平方メートルカバーできる。 tmlで描けるリングの面積を表す変数
    required_inks = 0 #黒リングのトータル面積
    n = 0 #ループ回数・リングをかける最大回数

    while paint > required_inks:
        #黒リングの半径はループ回数が一回増えるごとに2cmずつ増える
        r += 2 * n

        #ring = (r + 1) ** 2 * pi - r ** 2 * pi
        ring = (2 * r + 1) * pi
        required_inks += ring

        if required_inks > paint:
            break
        n += 1

    print(n)

input_file = open('bullseye.txt')

for i in range(int(input_file.readline())):
    output = input_file.readline().split(' ')
    r = int(output[0])
    t = int(output[1])
    calculate(r,t)



