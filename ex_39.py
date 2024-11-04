month = input().capitalize()
res = 0
m1 = ['Январь','Март','Май', 'Июль', 'Август','Октябрь','Декабрь']
m2 = ['Апрель', 'Июнь', 'Сентябрь', 'Ноябрь']
if month in m1:
    res = 31
elif month in m2:
    res = 30
else:
    res = '28 или 29'
print(f'{month} = {res}')


# я бы добавил .capitalize() в конце input()
