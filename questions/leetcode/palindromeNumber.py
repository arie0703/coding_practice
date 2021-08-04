

def isPalindrome(x: int) -> bool:
    s = str(x)


    if s[0] == "-":
        return False

    if len(s) % 2 > 0: #文字数が奇数
        center = len(s) // 2

        i = 0
        while center - i >= 0 and center + i < len(s):
            if s[center - i] != s[center + i]:
                return False
            i += 1

    else: 
        center = len(s) // 2
        if s[center] != s[center-1]:
            return False

        if len(s) == 2:
            return True
        
        i = 0
        while center - 1 - i >= 0 and center + i < len(s):
            if s[center-1-i] != s[center+i]:
                return False
            i += 1

    return True


print(isPalindrome(123))
print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(0))
print(isPalindrome(11511))
print(isPalindrome(11))
print(isPalindrome(1001))


        