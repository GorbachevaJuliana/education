num = int(input())
res = ''
if num < 2.0:
    res = 'минимальный уровень'
elif num > 2.0 and num < 3.0 or num == 2.0:
    res = 'очень слабый уровень'
elif num > 3.0 and num < 4.0 or num == 3.0:
    res = 'слабый уровень'
elif num > 4.0 and num < 5.0 or num == 4.0:
    res = 'промежуточный уровень'
elif num > 5.0 and num < 6.0 or num == 5.0:
    res = 'умеренный уровень'
elif num > 6.0 and num < 7.0 or num == 6.0:
    res = 'сильный уровень'
elif num > 7.0 and num < 8.0 or num == 7.0:
    res = 'очень сильный уровень'
elif num > 8.0 and num < 10.0 or num == 8.0:
    res = 'огромный уровень'
elif num == 10.0 or num > 10.0:
    res = 'разрушительный уровень'
print(res)