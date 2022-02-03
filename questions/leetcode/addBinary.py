def addBinary(a,b):

    res = ""
    carry = 0
    i = 1

    while i <= len(a) or i <= len(b):

        
        if i > len(a):
            n = int(b[-i]) + carry
        elif i > len(b):
            n = int(a[-i]) + carry
        else:
            n = int(a[-i]) + int(b[-i]) + carry
        res = str(n % 2) + res
        if n > 1:
            carry = 1
        else:
            carry = 0
        i += 1

    if carry == 1:
        res = str(carry) + res

    return res


print(addBinary("1010","101"))






