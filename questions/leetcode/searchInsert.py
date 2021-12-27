def searchFirst(idx, nums, target):
    
    while idx >= 0 and nums[idx] == target:
        idx -= 1
    return idx + 1

def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1


    if target <= nums[left]:
        return 0
    if target > nums[right]:
        return right + 1
    

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return searchFirst(mid, nums, target)
        elif nums[mid] < target:
            if nums[mid + 1] >= target:
                return mid + 1
            else:
                left = mid + 1
        else:
            if nums[mid - 1] < target:
                return mid
            elif nums[mid - 1] == target:
                print("a", mid)
                return searchFirst(mid - 1, nums, target)
            else:
                right = mid - 1

    return -1


print(searchInsert([1,2,3,4,5,10], 2))
