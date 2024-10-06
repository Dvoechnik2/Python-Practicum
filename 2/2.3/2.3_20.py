n = int(input())
hpre = 0
ind = -1
for i in range(n):
    b = int(input())
    h1 = b % 256
    r = (b // 256) % 256
    m = b // 65536
    h2 = (37 * (m + r + hpre)) % 256
    if h1 >= 100 or h1 != h2:
        if i < ind or ind == -1:
            ind = i
    hpre = h1
print(ind)
