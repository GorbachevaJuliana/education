m = input().capitalize()
d = int(input())
res = ''
if m == 'Январь' or m == 'Февраль' or m == 'Декабрь' and d >= 21: #or m == 'Март' and d < 20:
    res = 'Зима'
elif m == 'Март' and d < 20:
    res = 'Зима'
elif m == 'Март' and d >= 20:
    res = 'Весна'
elif m == 'Апрель' or m == 'Май' or m == 'Июнь' and d < 21:
    res = 'Весна'
elif m == 'Июнь' and d >= 21 or m == 'Июль' or m == 'Август' or m == 'Сентябрь' and d < 22:
    res =  'Лето'
else:
    res = 'Осень'
print(res)
