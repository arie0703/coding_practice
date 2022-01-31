def plusOne(digits):

    def advance(digits, i):
        digits[-i] = 0

        print(len(digits), i)
        if i == len(digits):
            digits.insert(0,1)
        elif digits[-i-1] == 9:
            advance(digits, i + 1)
        else:
            digits[-i-1] += 1

        
    if digits[-1] < 9:
        digits[-1] += 1
    else:
        advance(digits, 1)

    return digits

        



print(plusOne([1,8,9,9]))