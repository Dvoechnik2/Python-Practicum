x = input()
n = [int(x[i]) for i in range(3)]
n1 = sorted(n)
n2 = sorted(n, reverse=True)
n3 = [x for x in sorted(n) if x != 0]
nmax = str(n2[0]) + str(n2[1])
nmin = str(n1[0]) + str(n1[1]) if n1[0] != 0 else str(n3[0]) + '0'
print(nmin, nmax)
