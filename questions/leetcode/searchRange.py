def searchFirst(idx, nums, target):
    
    while idx >= 0 and nums[idx] == target:
        idx -= 1
    return idx + 1

def searchLast(idx, nums, target):
    
    while idx < len(nums) and nums[idx] == target:
        idx += 1
    return idx - 1
    

def searchRange(nums, target):

    left = 0
    right = len(nums) - 1
    ans = [-1, -1]

    while left <= right:
        mid = (left + right) // 2
        # print(mid)
        if nums[mid] == target:
            ans[0] = searchFirst(mid, nums, target)
            ans[1] = searchLast(mid, nums, target)
            return ans
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return ans


print(searchRange([5,7,7,8,8,10], 8))
print(searchRange([5,7,7,8,8,10], 6))
    