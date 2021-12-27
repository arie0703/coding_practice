# 動的計画法を使って解く

# https://leetcode.com/problems/longest-valid-parentheses/solution/
# Approach 2

def depthScan(s):
    d = [0 for _ in s]
    i = 0

    while i < len(s):
        
        if s[i] == ")":
            if i > 1:
                print(i, d, s)
                if d[i - 1] > 0 and s[i - d[i - 1] - 1] == "(" and i - d[i - 1] - 1 >= 0:
                    # print("参照するインデックス:", i - d[i - 1] - 1)
                    d[i] = d[i - 1] + 2
                elif d[i - 2] > 0 and s[i - d[i - 2] - 1] == "(" and i - d[i - 2] - 1 >= 0 and s[i - 1] == "(":
                    # print("参照するインデックス:", i - d[i - 2] - 1)
                    d[i] = d[i - 2] + 2
                elif s[i - 1] == "(":
                    d[i] = 2

                if i >= d[i] and d[i - d[i]] > 0:
                    # print (d[i - d[i]])
                    d[i] += d[i - d[i]]
            elif i == 1 and s[0] == "(":
                d[i] = 2

        i += 1
        

    return max(d)


def longestValidParentheses(s):
    
    if len(s) < 2:
        return 0
    return depthScan(s)

print(longestValidParentheses("(()))())("))

    