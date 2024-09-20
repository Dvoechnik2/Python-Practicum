a = int(input())
b = int(input())
c = int(input())
a, b, c = sorted([a, b, c])
if a ** 2 + b ** 2 == c ** 2:
    print('100%')
elif a ** 2 + b ** 2 > c ** 2:
    print('крайне мала')
else:
    print('велика')
