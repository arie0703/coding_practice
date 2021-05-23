def solve(n, score_list):
    return score_list

def answer():
    input_file = open('a1.txt')
    output_file = open('o1.txt','w')
    while True:
        n = int(input_file.readline())
        if n == 0:
            break
        score = []
        for i in range(n):
            score = score + [input_file.readline()]
        output_file.write(str(solve(n, score)) + '\n')
    input_file.close()
    output_file.close()
    return
    

answer()
