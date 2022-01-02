
def recursive(candidates, target, comb, ans):

    for i in range(len(candidates)):
        c = candidates[i]
            
        if target - c > 0:
            recursive(candidates[i+1:len(candidates)], target, comb[:], ans)
            comb.append(c)
            target -= c
            recursive(candidates[i:len(candidates)], target, comb[:], ans)
            
        elif target - c == 0:
            recursive(candidates[i+1:len(candidates)], target, comb[:], ans)
            comb.append(c)
            if not comb in ans:
                ans.append(comb)
            return ans
        else:
            break

    return ans


def combinationSum(candidates, target):
    ans = []
    candidates = sorted(candidates)
    for i in range(len(candidates)):
        temp = recursive(candidates[i:len(candidates)], target, [], [])
        # print(temp)
        for t in temp:
            if not t in ans:
                ans.append(t)
    
    return ans


"""
再帰だとちょっとメモリを食われるのでdfsを使った方が良い
https://leetcode.com/problems/combination-sum/discuss/1659301/Python-Solution
"""


def combinationDFS(candidates, target):
    res = []
    subset = []
    def dfs(i):
        print(subset)
        if i==len(candidates) or sum(subset)>target: return
        if target==sum(subset):
            res.append(subset[::])
            return
        subset.append(candidates[i])
        dfs(i)
        subset.pop()
        dfs(i+1)       
    dfs(0)
    return res


#candidates内の数字を重複して使用できない仕様
def combinationSum2(candidates, target):
    res = []
    subset = []

    candidates = sorted(candidates)
    def dfs(i):
        # print(i, subset)
        if target==sum(subset) and not subset in res:
            res.append(subset[::])
            return
        if i>=len(candidates) or sum(subset)>target: return
        subset.append(candidates[i])
        dfs(i+1) 

        subset.pop()
        while i < len(candidates) - 1:
            if (candidates[i] == candidates[i + 1]):
                i += 1
            else:
                break

        dfs(i + 1)
         
    dfs(0)
    return res

# print(combinationDFS([2,3,5], 8))
print(combinationSum2([8,7,4,3],11))
print(combinationSum2([10,1,2,7,6,1,5],8))
print(combinationSum2([2,5,2,1,2],5))
print(combinationSum2([1] * 30, 30))
# print(combinationDFS([2,3,6,7], 7))
# print(combinationDFS([2], 1))
# print(combinationDFS([3,5,8], 11))
# print(combinationDFS([2,7,6,3,5,1], 9))






    
    

            
