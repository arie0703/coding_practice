
def knap_dp(C, I, v, s):
    f = {}
    for c in range(0, C + 1):
        f[c] = 0
    print(f)
    for c in range(0, C + 1):
        for i in I:
            if c + s[i] <= C and f[c + s[i]] <= f[c] + v[i]:
                f[c]
                f[c + s[i]] = f[c] + v[i]
            print(f)
    return max(f.values())

C = 7
I = [1, 2, 3, 4]
v = {1: 16, 2: 19, 3: 23, 4: 28}
s = {1: 2, 2: 3, 3: 4, 4: 5}
print(knap_dp(C,I,v,s))

C = 7
I = [1, 2, 3, 4]
v = {1: 3, 2: 4, 3: 1, 4: 2}
s = {1: 2, 2: 3, 3: 1, 4: 3}

print(knap_dp(C,I,v,s))