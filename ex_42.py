n = input()
res = 0
if n == 'C4':
    res = 261,63
elif n == 'D4':
    res = 293,66
elif n == 'E4':
    res = 329,63
elif n == 'F4':
    res = 349,23
elif n == 'G4':
    res = 392,00
elif n == 'A4':
    res = 440,00
elif n == 'B4':
    res = 493,88
print(f'Частота ноты {n} равна {res}')
# У меня не получается сделать переменную res int(), а не turple()
