s = int(input('Введите громкость звука '))
if s > 130:
    print('Число больше максимального')
if s < 40:
    print('Число ниже минимального')
if s == 130:
    print('Отбойный молоток')
elif s == 106:
    print('Газовая газоокосилка')
elif s == 70:
    print('Будильник')
elif s == 40:
    print('Тихая комната')
if s < 130 and s > 106:
    print('Число находится между громкостью отбойного молотка и газовой газонокосилки')
elif s < 106 and s > 70:
    print('Число находится между громкостью газовой газонокосилки и будильника')
else:
    print('Число находится между будильника и тихой комнатой')
