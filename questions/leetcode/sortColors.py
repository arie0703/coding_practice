def sortColors(nums):
    # 選択ソート
    for i in range(len(nums)):
        minimum = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[minimum]:
                minimum = j
        nums[i], nums[minimum] = nums[minimum], nums[i]
    return nums

print(sortColors([1,2,0]))

