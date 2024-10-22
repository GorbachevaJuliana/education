C = 261.63
D = 293.66
E = 329.63
F = 349.23
G = 392.00
A = 440.00
B = 493.88
L = 1
num = float(input(''))
if num >= C - L and num <= C + L:
    res = 'C4'
elif num >= D - L and num <= D + L:
    res = "D4"
elif num >= E - L and num <= E + L:
    res = 'E4'
elif num >= F- L and num <= F + L:
    res = 'F4'
elif num >= G- L and num <= G + L:
    res = 'G4'
elif num >= A - L and num <= A + L:
    res = 'A4'
elif num >= B - L and num <= B + L:
    res = 'B4'
else:
    res = ''
if res == '':
    print('Ноты, соответствующей введенной частоте, не существует')
else:
    print(f'Введённая частота = ноте {res}')

