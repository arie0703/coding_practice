# https://leetcode.com/problems/two-sum/discuss/1373300/Python-Solution%3A-40-ms-14.4-MB

nums = [20,40,39,5,10,4,8,32,6,94,50,39,44,56,32,53,63,22,43,53,2,3,55,8,5,9]
target = 58

def twoSum(nums, target):
    # 辞書型でtargetからリストの各数字を引いた数とそのインデックス番号をペアで保存する
    look4 = {}
    for i in range(len(nums)):
        if nums[i] in look4: #リストのある数字が既に辞書の中にあり、
            if i != look4[nums[i]]: #インデックス番号がその数字のそれと異なるなら
                return [look4[nums[i]], i] #それが答え
        else:
            print(look4)
            look4[target-nums[i]] = i
    return []

print(twoSum(nums, target))