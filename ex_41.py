a = input('Введите длину первой стороны: ')
b = input('Введите длину второй стороны: ')
c = input('Введите длину третьей стороны: ')
if a == b and b == c:
    print('Это равносторонний треугольник')
elif a == b or b == c or c == a:
    print('Это равнобедренный треугольник')
else:
    print('Это разносторонний треугольник')
    










