def str_comp(f1, f2, l):
    return (h[f1 + l - 1] + h[f2 - 1] * x_pow[l]) % p \
           == (h[f2 + l - 1] + h[f1 - 1] * x_pow[l]) % p


s = input()
x = 43
p = 10 ** 9 + 7
h = [0] * (len(s) + 1)
h[0] = 0
x_pow = [0] * (len(s) + 1)
x_pow[0] = 1
for i in range(1, len(s) + 1):
    h[i] = (h[i - 1] * x + ord(s[i - 1])) % p
    x_pow[i] = (x_pow[i - 1] * x) % p
ans = [0]
for i in range(2, len(s) + 1):
    l, r = 0, len(s) - i + 1
    while l < r:
        m = (l + r + 1) // 2
        if str_comp(1, i, m):
            l = m
        else:
            r = m - 1
    ans.append(l)
print(*ans)
