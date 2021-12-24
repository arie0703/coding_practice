# 通常のreverse
def reverse(arr):
    temp = arr
    count = len(arr)
    prev = []
    while count > 0:
        prev.insert(0, temp.pop(0))
        print(prev, temp)
        count -= 1

    return prev

#k回ごとにreverse
def reversePerK(arr, k):

    group = len(arr) // k
    temp = arr
    count = k
    prev = []
    ans = []

    for _ in range(group):
        while count > 0:
            prev.insert(0, temp.pop(0))
            print(prev, temp)
            count -= 1
        count = k
        ans.extend(prev)
        prev = []

    if temp:
        ans.extend(temp)
    return ans


print(reversePerK([1,2,3,4,5],2))
print(reversePerK([1,2,3,4,5,6,7],3))
