line = input()
x, y = 0, 0
while line != 'СТОП':
    n = int(input())
    if line[0] == 'С':
        y += n
    if line[0] == 'В':
        x += n
    if line[0] == 'Ю':
        y -= n
    if line[0] == 'З':
        x -= n
    line = input()
print(y)
print(x)