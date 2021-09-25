# 1000(900) -> 500(100) -> 100(90) -> 50(10) -> 10(9) -> 5(4)


def intToRoman(num):

    reminder = num
    idx = 0
    n_list = [1000, 500, 100, 50, 10, 5, 1]
    prenum = 900
    char_list = ["M", "D", "C", "L", "X", "V", "I"]
    pre_char = char_list[2]
    ans = ""

    while reminder > 0:
        char = char_list[idx]
        n = n_list[idx]

        if n == 1: # nが1ならIをくっつけてreturn
            ans = ans + (char * reminder)
            return ans

        if idx % 2 > 0: #500, 50, 5
            prenum = int(n * 0.8)
        else: # 1000, 100, 10
            prenum = int(n * 0.9)

        if pre_char == char: # M(C) -> D(C) -> C(X) -> L(X) -> X(I) -> V(I)
            pre_char = char_list[idx + 2]

        quantity = reminder // n
        reminder = reminder % n

        if quantity > 0 and reminder < prenum:
            ans = ans + (char * quantity)
        if reminder >= prenum:
            ans = ans + (char * quantity) + pre_char + char
            reminder %= prenum

        idx += 1
    return ans
        

def intToRomanEx(num):
        
    numeral_map = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }
    
    # Use integer division to get the number of multiples of the value in the number

    roman = ""
    for value in numeral_map.keys():
        multiplier = num // value
        print(multiplier)
        if multiplier > 0:
            roman += numeral_map[value] * multiplier  # Add the roman numeral multiplyer times
            num %= value
    
    return roman



print(intToRomanEx(1994))
print(intToRomanEx(58))
print(intToRomanEx(3999))
