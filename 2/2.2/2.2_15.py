a = int(input())
a = [a // 10, a % 10]
b = int(input())
b = [b // 10, b % 10]
nmax = max(a + b)
nmin = min(a + b)
nsr = (sum(a) + sum(b) - nmin - nmax) % 10
print(str(nmax) + str(nsr) + str(nmin))