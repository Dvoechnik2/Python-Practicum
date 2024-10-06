a = float(input())
s = 0
while a != 0:
    if a >= 500:
        s += (a * 0.9)
    else:
        s += a
    a = float(input())
print(s)