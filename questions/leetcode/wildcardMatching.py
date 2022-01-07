def isMatch(s,p):

    def dp(i,j):
        print(i,j)
        if i == len(s) and j >= len(p):
            return True
        if j == len(p):
            return False
        if i == len(s):
            if p[j] == '*':
                return dp(i, j+1)
            return False
        if p[j] != '*' and p[j] != '?':
            if s[i] != p[j]:
                return False
        if p[j] == '*':
            if  dp(i + 1, j) or dp(i, j + 1):
                return True
        return dp(i + 1, j + 1)

    ans = dp(0,0)

    return ans





p = 'aa*a*'
s = 'aababaccc'

print(isMatch(s,p))

