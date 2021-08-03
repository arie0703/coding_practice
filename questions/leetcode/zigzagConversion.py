def convert(s, numRows):
    arr = ["" for _ in range(numRows)]
    i = 0
    while i < len(s):

        for j in range(numRows): #縦に文字列を埋める処理
            if i >= len(s): break
            print(s[i], arr)
            arr[j] += s[i]
            i += 1
        
        for k in range(numRows - 2):
            if i >= len(s): break
            print(s[i], arr)
            arr[numRows - 2 - k] += s[i]
            i += 1

    ans = ""
    for l in range(len(arr)):
        ans += arr[l]


    return ans


t1 = "PAYPALISHIRING"
t2 = 3

t3 = "PAYPALISHIRING"
t4 = 4

t5 = "A"
t6 = 1

print(convert(t1, t2))
print(convert(t3, t4))
print(convert(t5, t6))