from itertools import permutations

def permute_with_itertools(nums):
    per = list(permutations(nums))
    res = []
    for p in per:
        res.append(list(p))

    return res

# itertoolsを使わずにpermutationを実装する
# 参考: https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/

import copy
def permute(nums):
    res = []
    def make_permutation(target, end):
        if target == end and not nums in res: 
            res.append(copy.deepcopy(nums))
        else: 
            for i in range(target, end): 
                print(target, i)
                nums[target], nums[i] = nums[i], nums[target] 
                make_permutation(target + 1, end) 
                nums[target], nums[i] = nums[i], nums[target]  # backtrack 
    
    make_permutation(0, len(nums))
    return res

nums = [1,2,3,4]
# print(permute(nums))



# 1からnまでのリストの辞書式並び替えで、k番目を取得する
# nextPermutationのコードを再利用
def getPermutation(n, k):
    sorted_list = [str(i) for i in range(1, n + 1)]

    import math
    #この関数は与えられたリストに重複した数字がない場合有効
    permutated = []
    d = len(sorted_list) - 1 # 上からn桁目から末尾までの数字の個数
    k = k - 1

    while d > 0:
        p = math.factorial(d) #階乗を取得
        i = k // p
        print(p,i)
        permutated.append(sorted_list.pop(i))
        d -= 1
        k -= (p * i)

        if k == 0:
            permutated.extend(sorted_list)
            break

    return "".join(permutated)
print(getPermutation(10,3004))
        


