# https://leetcode.com/problems/string-to-integer-atoi/

def myAtoi(s: str) -> int:
    
    numAlreadyAppeared = False #数字がすでに一回以上読み取られたか
    plusminusAlreadyAppeared = False
    ans = ""
    for char in s:
        if char == " ": #空白はスルー
            if numAlreadyAppeared or plusminusAlreadyAppeared: #既に符号か数字が出ているなら状態ならbreak
                break
        elif char == "0" and not numAlreadyAppeared: #数字が一度も出てきてない状態で0が出てきたら
            numAlreadyAppeared = True #数字が既に読み取られた判定はしておく。
        elif char == "+" or char == "-": #符号が出てきたら・・
            if numAlreadyAppeared or plusminusAlreadyAppeared: #既に符号か数字が出ているなら状態ならbreak
                break

            plusminusAlreadyAppeared = True
            if char == "-" and not numAlreadyAppeared:
                ans += "-"
        elif not char.isdigit():#数字じゃなかったら強制終了
            break
        else:
            ans += char
            if not numAlreadyAppeared:
                numAlreadyAppeared = True
            if int(ans) > 2 ** 31 - 1: #clamp
                return 2 ** 31 - 1
            elif int(ans) < -2 ** 31:
                return -2 ** 31
        
        
    try:
        int(ans) #現状のansが数字に変換できるか
    except:
        return 0 #できなければ0を返す
    return int(ans)



print(myAtoi("   49003"))
print(myAtoi("4193 with words"))
print(myAtoi("words and 987"))
print(myAtoi("-91283472332"))
print(myAtoi("   -42"))
print(myAtoi("  -0042"))
print(myAtoi("3.14159"))
print(myAtoi("+-12"))
print(myAtoi("--12"))
print(myAtoi("-1+2"))
print(myAtoi("00000-42a1234"))
print(myAtoi("+0 123"))
print(myAtoi("4 123"))
print(myAtoi("  + 123"))
