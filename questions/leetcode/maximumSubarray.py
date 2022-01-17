def maxSubArray(nums):
    if max(nums) < 0:
        return max(nums)
        
    maximum, presum = 0,0
    for i in nums:
        print(i, presum, maximum)
        presum = max(0,presum+i) # あるインデックスから一つ前までの数字の合計値（0を下回ったら次の数字からカウントするようにする）
        maximum = max(maximum, presum)
            
    return maximum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

