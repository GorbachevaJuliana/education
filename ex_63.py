numbers = int(input())
list = []
if numbers == 0: 
    print('Ошибка')
while numbers != 0:
    numbers = int(input())
    list.append(numbers)
if 0 in list:
    list.remove(0)
print(list)
print(sum(list))
print(len(list))
print(f'Среднее значение: {sum(list) / len(list)}')

# Если первым числом будет 0 - то будет ошибка ZeroDivisionError: division by zero
# Первое число не учитывается при подсчете среднего
