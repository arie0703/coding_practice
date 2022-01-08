def jump(nums):

    now = c =  0

    while now < len(nums) - 1:
        jump = nums[now]
        farthest = 0
        next_idx = 0
        for i in range(now + 1, now + jump + 1):
            #現在地の数字から飛べる範囲で、任意の場所のindexと数字を足した数字が一番大きいところを次の移動開始位置とする
            print("range", now + 1, now + jump + 1)
            if i >= len(nums) - 1:
                print("break")
                return c + 1
            print(nums[i], i)
            if i + nums[i] > farthest:
                farthest = i + nums[i]
                next_idx = i
        

        now = next_idx #次の位置
        print("次は", now)
        c += 1
    return c
        

    

print(jump([1,1,1,1]))
print(jump([2,3,0,1,4]))
print(jump([9,7,9,4,8,1,6,1,5,6,2,1,7,9,0]))

        
        