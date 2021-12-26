import math
#この関数は与えられたリストに重複した数字がない場合有効
def permutationToNums(k, sorted_list): # sortされたリストから辞書式でk番目のリストを返す
    permutated = []
    d = len(sorted_list) - 1 # 上からn桁目から末尾までの数字の個数
    k = k - 1

    while d > 0:
        p = math.factorial(d)
        i = k // p
        permutated.append(sorted_list.pop(i))
        d -= 1
        k -= (p * i)

        if k == 0:
            permutated.extend(sorted_list)
            break

    return permutated



def nextPermutation(nums):

    # 配列の後ろから数字を参照し、後ろから数字が大きくなる流れが終わるインデックスを取得
    def find_decreasing_sequence_end():
        # return i where nums[i+1] < nums[i] from i+1..n
        i = len(nums)-1
        
        # precondition: i is last element in array
        while i >= 0 and nums[i-1] >= nums[i]:
            i -=1
        # postcondition: nums[i-1] < nums[i]
        print(i-1)
        return i-1
    
    def find_next_greater_number_from(start):
        target = nums[start]
        # find the next greatest number for target
        # in a[start..n]
        # precondition: a[n..start) is strictly decreasing
        for i in range(len(nums)-1, start, -1):
            if nums[i] > target:
                return i
        # postcondition: no greatest number, impossible
        return -1
    
    def swap(a, b):
        nums[a], nums[b] = nums[b], nums[a]
    
    def reverse(begin, end):
        # reverses array inplace from [begin, end]
        i, j = begin, end
        
        
        while i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
    
    # 配列の後ろから一桁ずつ見ていって、任意の桁の一個上の桁が任意の桁より小さくなる桁のインデックスを取得
    next_option_index = find_decreasing_sequence_end()
    # 大きい順だったらリバースしてreturn
    if next_option_index < 0:
        # theres no next permutation
        # just reverse the array
        reverse(begin=0, end=len(nums)-1)
        print(nums)
        return

    # 配列を後ろから参照していき、next_option_indexより大きい数字を返す
    next_greater_index = find_next_greater_number_from(next_option_index)
    # 入れ替え
    swap(next_option_index, next_greater_index)
    # 任意の桁kから配列の末尾までひたすら入れ替えする
    reverse(begin=next_option_index+1, end=len(nums)-1)
    print(nums)



print(nextPermutation([2,1,4,3])) # 2, 3, 1, 4



