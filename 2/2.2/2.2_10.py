n = int(input())
n1 = n // 100 + (n // 10) % 10
n2 = (n // 10) % 10 + n % 10
print(str(max(n1, n2)) + str(min(n1, n2)))