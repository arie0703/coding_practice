def firstMissingPositive(nums):
    nums = sorted(nums)
    pre = -1

    if nums[0] > 1 or max(nums) < 1:
        return 1

    for n in nums:
        if n - 1 > pre and n > 1:

            if pre > 0:
                return pre + 1
            else:
                return 1

        pre = n
    return nums[-1] + 1

# https://leetcode.com/problems/first-missing-positive/discuss/1665625/Python-O(n)-time-O(n)-extra-space

def betterSolution(nums):
    length = len(nums)

    #boolのリストを作る
    bool_list = [False] * (length+1)

    
    for n in nums:
        """
        numsの中身を一個ずつ見ていく
        各数字が0以上,numsのlength以下なら、その数字に対応したbool_listのインデックスをTrueにする
        
        nが2なら、bool_lis[n] = Trueとなり、「numsの中に2はあるよ！」ってことになる。
        """
        if 0 < n <= length:
            bool_list[n] = True

    print(bool_list)

            
    for i in range(1, length+1):

        """
        bool_listを一個ずつ見ていく。
        例えば、1がnumsになかったらbool_list[1]はFalseになっているので1が返される
        """
        if not bool_list[i]:
            return i
        
    return length+1

# print(betterSolution([3,4,-1,1]))
# print(betterSolution([1,2,0]))
# print(betterSolution([7,8,9,2,1]))