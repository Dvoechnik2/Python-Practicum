lf , rt = 0, 1001
line = ''
while line != 'Угадал!':
    c = (lf + rt) // 2
    print(c)
    line = input()
    if line[0] == 'Б':
        lf = c
    if line[0] == 'М':
        rt = c

