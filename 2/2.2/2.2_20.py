line = 'яяя' * 100000
for x in range(3):
    ln = input()
    if 'зайка' in ln and ln < line:
        line = ln
print(line, len(line))