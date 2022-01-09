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
print(permute(nums))


