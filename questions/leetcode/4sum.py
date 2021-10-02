def fourSum(nums, target):

    nums.sort()
    N, result = len(nums), []
    for i in range(N): 
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        for j in range(i + 1, N):
            temp = target - (nums[i] + nums[j])

            s,e = j+1, N-1
            while s<e:
                if nums[s]+nums[e] == temp:
                    arr = [nums[i], nums[j], nums[s], nums[e]]
                    if not arr in result:
                        result.append([nums[i], nums[j], nums[s], nums[e]])
                    s = s+1
                    while s<e and nums[s] == nums[s-1]:
                        s = s+1
                elif nums[s] + nums[e] < temp:
                    s = s+1
                else:
                    e = e-1
    return result

print(fourSum([2,2,2,2,2], 8))
print(fourSum([1,0,-1,0,-2,2], 0))
print(fourSum([1,2,3,4,5], 10))