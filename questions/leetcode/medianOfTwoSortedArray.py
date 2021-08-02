# https://leetcode.com/problems/median-of-two-sorted-arrays/

def findMedianSortedArrays(nums1, nums2):
    l = sorted(nums1 + nums2)
    length = len(l)
    ans = 0
    if length % 2 == 0:
        if (l[int(length / 2)] + l[int(length / 2) - 1]) != 0:
            ans = (l[int(length / 2)] + l[int(length / 2) - 1]) / 2
        else:
            return ans
    else:
        ans = l[int(length / 2)]

    return ans



e1, e2 = [1,3],[2]
e3, e4 = [1,2], [3,4]
e5, e6 = [0,0], [0,0]
e7, e8 = [], [1]
print(findMedianSortedArrays(e1, e2))
print(findMedianSortedArrays(e3, e4))
print(findMedianSortedArrays(e5, e6))
print(findMedianSortedArrays(e7, e8))