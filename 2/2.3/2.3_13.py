n = int(input())
name = ''
for i in range(n):
    s = input()
    if s < name or name == '':
        name = s
print(name)