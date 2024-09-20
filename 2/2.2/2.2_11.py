x = input()
n = [int(x[i]) for i in range(3)]
m = min(n) + max(n)
s = sum(n) - m
if s * 2 == m:
    print('YES')
else:
    print('NO')
