import itertools


def maxArea(height) -> int: # My answer 結果はTLE
    index = len(height)
    D = {i: 0 for i in range(index)}
    for i in range(index):
        D[i] = height[i]
    # print(D) # これでindexとheightペア完成
    idx_list = [i for i in range(index)]
    conbinations = list(itertools.combinations(idx_list,2))
    ans = 0
    for c in conbinations:
        if D[c[0]] > D[c[1]]:
            smaller = D[c[1]]
        else:   
            smaller = D[c[0]]

        dist = c[1] - c[0]
        temp = smaller * dist

        # print(temp)

        if temp > ans:
            ans = temp
    
    return ans

def maxAreaByGenious(height):
    # LeetcodeのDiscussionより
    # https://leetcode.com/problems/container-with-most-water/discuss/1473487/python-two-pointers-solution-time-O(N)-space-o(1)
    result, low, high = 0, 0, len(height) -1
    # low, highはそれぞれindex
    while low < high:
        print(low, high) #右端・左端から狭めていくイメージ
        result = max(result, min(height[low], height[high]) * (high - low))
        if height[low] < height[high]:
            low += 1
        else:
            high -= 1
    return result


print(maxAreaByGenious([4,3,2,1,4]))
print(maxAreaByGenious([1,8,6,2,5,4,8,3,7]))
print(maxAreaByGenious([1,1]))