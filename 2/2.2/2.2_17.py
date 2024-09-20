a = float(input())
b = float(input())
c = float(input())
d = (b ** 2 - 4 * a * c)
if a == 0:
    if b == 0:
        if c == 0:
            print('Infinite solutions')
        else:
            print('No solution')
    else:
        print(f'{-c / b:.2f}')
elif d > 0:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print(f'{min(x2, x1):.2f}', f'{max(x1, x2):.2f}')
elif d == 0:
    print(f'{-b / (2 * a):.2f}')
else:
    print('No solution')
