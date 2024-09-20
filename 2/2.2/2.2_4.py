n1 = (int(input()), 'Петя')
n2 = (int(input()), 'Вася')
n3 = (int(input()), 'Толя')
a = sorted([n1, n2, n3], key=lambda x: x[0], reverse=True)
a = [f'{i + 1}. {a[i][1]}' for i in range(3)]
print(*a, sep='\n')