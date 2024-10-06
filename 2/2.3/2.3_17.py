s = input()
line =''
for x in s:
    if int(x) % 2 != 0:
        line += x
print(line)