month = input()
res = 0
if month == 'Январь' or month == 'Март' or month == 'Май' or month == 'Июль' or month == 'Август' or month == 'Октябрь' or month == 'Декабрь':
    res = 31
elif month == 'Апрель' or month == 'Июнь' or month == 'Сентябрь' or month == 'Ноябрь':
    res = 30
else:
    res = '28 или 29'
print(f'{month} = {res}')

# сделай через списки, чтобы эти длинные строки (3 и 5) исчезли 
