k = 0
a = input()
while a != 'Приехали!':
    k += 1 if 'зайка' in a else 0
    a = input()
print(k)