n = int(input())
c = []
i = 2
while n != 1:
    if n % i == 0:
        c.append(i)
        n //= i
        i = 2
    else:
        i += 1
print(*c, sep=' * ')