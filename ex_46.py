a = 'abcdefgh'
l = a.index(input("Введите букву: ")) + 1
n = int(input("Введите цифру: "))
if (n + l) % 2:
    print('белая')
else:
    print('чёрная')