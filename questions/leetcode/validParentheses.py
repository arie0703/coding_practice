# https://leetcode.com/problems/valid-parentheses/

def compare(s):
    l = ["()", "{}", "[]"]
    pre = ""
    chars = s
    for i in range(len(s)):
        print(i, s[i])
        pair = pre + s[i]
        print("pair: ", pair)
        if pair in l:
            print("yeah")
            chars = chars.replace(pair, "")
        pre = s[i]
    
    if len(chars) == 0 or s == chars:
        return chars
    else:
        print("再起", chars)
        return compare(chars)


def isValid(s):
    chars = compare(s)
    print(chars)
    if not chars:
        return True
    else:
        return False
    
    
    

print(isValid("(){}{"))
