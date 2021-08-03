
def longestPalindrome(s: str):
    records = []
    records_length = []
    for i in range(len(s)):
        center = s[i] #調査対象の文字、これを真ん中として調査する
        r = 1
        while i-r >= 0 and i+r < len(s) and s[i-r] == s[i+r]: #偶数の回文を探す
            center = s[i-r] + center + s[i+r]
            r += 1
        records.append(center)
        records_length.append(len(center))
        center = s[i]
        r = 1
        if i + 1 < len(s) and s[i] == s[i + 1]: #次の文字が同じ文字ならそれら二つの文字列を真ん中とする
            center = s[i] + s[i+1]
            while i-r >= 0 and i+1+r < len(s) and s[i-r] == s[i+1+r]: #奇数の回文を探す
                center = s[i-r] + center + s[i+1+r]
                r += 1
        records.append(center)
        records_length.append(len(center))

    
    idx = records_length.index(max(records_length))
    ans = records[idx]

    return ans

t1 = "babad"
t2 = "cbbd"
t3 = "a"
t4 = "ac"
t5 = "aaabbbbbckckckuiuiddddiuiu"
t6 = "sksksksksksksksksksksksksk"
t7 = "aiueoooeuiayeahaiueooooeuia"


print(longestPalindrome(t1))
print(longestPalindrome(t2))
print(longestPalindrome(t3))
print(longestPalindrome(t4))
print(longestPalindrome(t7))

