def trap(height):
    left = 0
    right = len(height) - 1

    max_left, max_right = 0, 0
    ans = 0

    while left < right:
        max_left = max(max_left, height[left])
        max_right = max(max_right, height[right])

        if max_left < max_right:

            ans += max_left - height[left]
            print(left, max_left, height[left], ans)
            left += 1

        else:
            ans += max_right - height[right]
            print(right, max_right, height[right], ans)
            right -= 1
        
    return ans

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
