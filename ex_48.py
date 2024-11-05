day = int(input())
month = input()
if month == 'Декабрь' and day >= 22 or month == 'Январь' and day <= 19:
    res = 'Козерог'
elif month == 'Январь' and day >= 20 or month == 'Февраль' and day <= 18:
    res = 'Водолей'
elif month == 'Февраль' and day >= 19 or month == 'Март' and day <= 20:
    res = 'Рыбы'
elif month == 'Март' and day >= 21 or month == 'Апрель' and day <= 19:
    res = 'Овен'
elif month == 'Апрель' and day >= 20 or month == 'Май' and day <= 20:
    res = 'Телец'
elif month == 'Май' and day >= 21 or month == 'Июнь' and day <= 20:
    res = 'Близнецы'
elif month == 'Июнь' and day >= 21 or month == 'Июль' and day <= 22:
    res = 'Рак'
elif month == 'Июль' and day >= 23 or month == 'Август' and day <= 22:
    res = 'Лев'
elif month == 'Август' and day >= 23 or month == 'Сентябрь' and day <= 22:
    res = 'Дева'
elif month == 'Сентябрь' and day >= 23 or month == 'Октябрь' and day <= 22:
    res = 'Весы'
elif month == 'Октябрь' and day >= 23 or month == 'Ноябрь' and day <= 21:
    res = 'Скорпион'
elif month == 'Ноябрь' and day >= 22 or month == 'Декабрь' and day <= 21:
    res = 'Стрелец'
print(f'Ваш знак зодиака - {res}')
