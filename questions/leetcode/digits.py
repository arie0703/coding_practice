import itertools

def letterCombinations(digits):

    if not digits:
        return  []
    D = {'2':['a','b','c'],
        '3':['d','e','f'],
        '4':['g','h','i'],
        '5':['j','k','l'],
        '6':['m','n','o'],
        '7':['p','q','r','s'],
        '8':['t','u','v'],
        '9':['w','x','y','z']}

    comb = [D[i] for i in digits] 
    ans = list(map(''.join, (itertools.product(*comb))))
    return ans

    


print(letterCombinations("23"))
print(letterCombinations(""))
print(letterCombinations("2"))
print(letterCombinations("435"))
print(letterCombinations("4359"))