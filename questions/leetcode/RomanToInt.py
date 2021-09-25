def romanToInt(s):
    num = 0
    d = {
        900: 'CM',
        400: 'CD',
        90: 'XC',
        40: 'XL',
        9: 'IX',
        4: 'IV',
        1000: 'M',
        500: 'D',
        100: 'C',
        50: 'L',
        10: 'X',
        5: 'V',
        1: 'I'
    }

    for n in d.keys():
        # n = 数字　d[n] = ローマ数字
        add = s.count(d[n]) # 任意のローマ数字の出現回数
        num += n * add # ローマ数字の出現回数 * 対応する数字を足していく
        s = s.replace(d[n], "")
    return num


print(romanToInt('MCMXCIV'))
print(romanToInt("LVIII"))
print(romanToInt("IX"))
