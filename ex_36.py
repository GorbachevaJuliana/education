a = int(input())
if a < 0:
    print('ошибка')
elif a == 1:
    res = 10.5
elif a == 2:
    res = 10.5 * 2
elif a == 3:
    res = (10.5 * 2) + 4
else:
    res = 10.5 * 2 + 4 * (a - 2)
print(res)