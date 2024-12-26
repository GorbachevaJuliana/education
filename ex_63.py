numbers = int(input())
list = []
if numbers == 0: 
    print('Ошибка')
    exit()
else:
    list.append(numbers)
while numbers != 0:
    numbers = int(input())
    list.append(numbers)
if 0 in list:
    print('Ошибка')
    list.remove(0)
print(list)
print(sum(list))
print(len(list))
print(f'Среднее значение: {sum(list) / len(list)}')

