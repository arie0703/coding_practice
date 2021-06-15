Y = [3 ** i for i in range(10)]
print(Y)

Z = [(x, y) for x in [1, 2, 3] for y in ['a', 'b', 'c']] # [1, 2, 3]と['a', 'b', 'c']の直積
print(Z)

kuku = [[x * y for x in range(1, 10)] for y in range(1, 10)] # いわゆる掛け算九九の表
print(kuku)

X = [i for i in range(20) if i % 2 != 0 and i % 3 != 0] # 0から19の整数のうち，2でも3でも割り切れないもの
print(X)

D = {i: str(i) for i in range(10)} # 整数がキーで，その整数の文字列化したものを値とする辞書
print(D)