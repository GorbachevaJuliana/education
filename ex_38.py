side = int(input('Напишите количество сторон у фигуры'))
if side < 3 or side > 10:
    print('Введите другое число.')
    exit()
if side == 3:
    print('треугольник')     
elif side == 4:
    print('четырёхугольник')
elif side == 5:
    print('пятиугольник')
elif side == 6:
    print('шестиугольник')
elif side == 7:
    print('семиугольник')
elif side == 8:
    print('восьмиугольник')
elif side == 9:
    print('девятиугольник')
elif side == 10:
    print('десятиугольник')