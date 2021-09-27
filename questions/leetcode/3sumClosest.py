def threeSumClosest(nums, target):
    result = 0
    min_gap = 99999

    nums.sort()
    N = len(nums)
    for i in range(N):
        
        start, end = i+1, N-1
        t = target - nums[i]
        while start < end:
            if nums[start] + nums[end] == t:
                return target
            gap = abs(t - (nums[start] + nums[end]))
            if gap < min_gap:
                min_gap = gap
                result = nums[i] + nums[start] + nums[end]

            elif nums[start] + nums[end] < t:
                start += 1
            else:
                end -= 1
            
    return result

print(threeSumClosest([-1,2,1,-4], 1))
print(threeSumClosest([0,1,2], 3))
print(threeSumClosest([1,1,-1,-1,3], 3))