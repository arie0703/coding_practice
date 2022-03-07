import math

def climbStairs(n):
    res = 0
    count_of_two = 0
    while count_of_two * 2 <= n:
        count_of_one = n - (count_of_two * 2)
        perm = math.factorial(count_of_two + count_of_one) // (math.factorial(count_of_two) * math.factorial(count_of_one))
        res += perm
        count_of_two += 1
    return res

print(climbStairs(2))