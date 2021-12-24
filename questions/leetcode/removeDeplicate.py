#ソートされた配列から被った数字を削除
#別の配列を用意せず、与えられたリストから数字を削除する形式にしなければならない

def removeDuplicates(nums):
    duplicates = []
    i = 0
    while i < len(nums):

        if nums[i] in duplicates:
            c = nums.count(nums[i])
            print(nums)
            print("del:", i+1, i+c-1)
            print(nums[i : i+c-1], "が削除される")
            del nums[i : i + c - 1]
            
        else:
            duplicates.append(nums[i])
            i += 1
        
    return nums

# print(removeDuplicates([1,1,2]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
