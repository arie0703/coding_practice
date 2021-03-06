def jump(nums):

    now = c =  0

    while now < len(nums) - 1:
        jump = nums[now]
        farthest = 0
        next_idx = 0

        if nums[now] == 0:
            print("Last Indexに辿り着くのは不可能")
            return -1

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
        

    

# print(jump([1,1,1,1]))
# print(jump([2,3,0,1,4]))
# print(jump([9,7,9,4,8,1,6,1,5,6,2,1,7,9,0]))

# Greedy
def canJump(nums):
    j = 0

    # j = 一個前のインデックスから飛べる最大のインデックスを表す
    for i, n in enumerate(nums):
        print(i,n,j)

        # jが現在のインデックスを上回っている場合、進行不可となる
        if j < i: 
            return False
        
        j = max(j, i+n)
    return True


# print(canJump([1,1,1,1]))
# print(canJump([2,3,0,1,4]))
# print(canJump([9,7,9,4,8,1,6,1,5,6,2,1,7,9,0]))
print(canJump([3,2,1,0,4]))


        
        