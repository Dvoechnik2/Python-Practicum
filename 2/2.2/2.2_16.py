p = (int(input()), 'Петя')
v = (int(input()), 'Вася')
t = (int(input()), 'Толя')

m = [x[1] for x in sorted([p, v, t], key=lambda x: x[0], reverse=True)]

print(f'          {m[0]}')
print(f'  {m[1]}')
print(f'                  {m[2]}  ')
print(f'   II      I      III   ')
