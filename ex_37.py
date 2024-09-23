let = str(input('Введите букву')).lower()
v = ['a', 'e', 'i', 'o', 'u']
if let == 'y':
    print('Буква может быть и гласной и согласной.')
elif let in v:
    print('Гласная.')
else:
    print('Согласная')

