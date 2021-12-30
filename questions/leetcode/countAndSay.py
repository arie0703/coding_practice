def countAndSay(n):

    def recursive(val):
        c = 1
        pre = val[0]
        digit = ""

        for i in range(1, len(val)):
            if val[i] != pre:
                digit += (str(c) + pre)
                c = 1
                pre = val[i]
            else:
                c += 1
        
        digit += (str(c) + pre)

        return digit

    if n > 1:
        val = "1"
        for _ in range(n - 1):
            val = recursive(val)
    else:
        return "1"

    return val



            
print(countAndSay(5))

                
            