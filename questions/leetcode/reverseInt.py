def reverse(x: int) -> int:
    s = str(x) #一桁ずつループで参照するためにstrに変換
    ans = ""
    for i in range(len(s)-1,-1,-1):
        
        if i == len(s) - 1 and s[i] == "0" and len(s) > 1:
            continue
        elif s[i] == "-":
            ans = "-" + ans
        else:
            ans += s[i]

    if int(ans) < -2 ** 31 or int(ans) > 2 ** 31:
        return 0
    
    return int(ans)

print(reverse(203))
print(reverse(-203))
print(reverse(2030))
print(reverse(0))
print(reverse(-1145140))
print(reverse(1534236469))

print(2 ** 31 - 1)
print(-2 ** 31)

