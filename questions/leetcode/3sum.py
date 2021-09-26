import itertools

def threeSumD(nums): #没 TLE
    if len(nums) < 3:
        return []
    nums.sort()
    lis = list(itertools.combinations(nums,3))
    ans = []
    for l in lis:
        if sum(l) == 0 and not list(l) in ans:
            ans.append(list(l))
    return ans

def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]

    numsの要素の個数だけループ回す
    ソートしたnumsの最後尾（最大値）はnum[N]とする
    nums[i]と (num[i+n] + num[N])を足して0になるなら答えリストにappend
    itertools使うより計算量少ないと思われる。
    """
    nums.sort()
    N, result = len(nums), []
    for i in range(N):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        target = nums[i]*-1
        s,e = i+1, N-1
        while s<e:
            if nums[s]+nums[e] == target:
                result.append([nums[i], nums[s], nums[e]])
                s = s+1
                while s<e and nums[s] == nums[s-1]:
                    s = s+1
            elif nums[s] + nums[e] < target:
                s = s+1
            else:
                e = e-1
    return result


print(threeSum([-2,0,1,1,2]))
# print(threeSumD([-1,0,1,2,-1,-4]))
# print(threeSum([4,4,-1,4,-1]))
# print(threeSum([0,1,0,-3,1,1]))





