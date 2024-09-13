n = int(input())
line = f'Я больше никогда не буду писать "{input()}"!'
print(line + ('\n' + line) * (n - 1))