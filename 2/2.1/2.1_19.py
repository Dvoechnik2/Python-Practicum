item = input()
c = int(input())
v = int(input())
m = int(input())
print('================Чек================')
print('Товар:' + ' ' * (29 - len(item)) + item)
print('Цена:' + ' ' * (19 - len(str(c)) - len(str(v))) + f'{v}кг * {c}руб/кг')
print('Итого:' + (26 - len(str(v * c))) * ' ' + f'{v * c}руб')
print('Внесено:' + ' ' * (24 - len(str(m))) + f'{m}руб')
print('Сдача:' + ' ' * (26 - len(str(m - v * c))) + f'{m - v * c}руб')
print('=' * 35)