#https://codingcompetitions.withgoogle.com/codejam/round/0000000000432b33/0000000000432cd2

t1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
t2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
t3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv"


def translation(text):
    table = str.maketrans({
        'a':'y', 'b':'h', 'c':'e', 'd':'s', 'e':'o',
        'f': 'c', 'g': 'v', 'h':'x', 'i':'d', 'j':'u',
        'k':'i', 'l':'g', 'n':'b', 'm':'l', 'o':'k',
        'p':'r', 'q':'z', 'r': 't', 's':'n', 't':'w',
        'u':'j', 'v':'p', 'w': 'f', 'x':'m', 'y':'a', 'z':'q'
    })

    print(text.translate(table))

translation(t1)
translation(t2)
translation(t3)