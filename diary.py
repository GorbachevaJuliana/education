import datetime
import os
import win10toast
toaster = win10toast.ToastNotifier()
def diary_write(message = ''):
    file = open('diary.txt', 'a', encoding = 'utf-8')
    while message != 'Stop' and message != 'Стоп':
        message = input().capitalize()
        if message == 'Delete' or message == 'Удалить':
            file.close()
            os.remove('D:\dates_titles\diary.txt')
            return
        date = datetime.datetime.now()
        date_str = datetime.datetime.strftime(date, '%d %m %Y %H-%M')
        file.write(f'{date_str}: {message} \n')
    file.close()
    return
diary_write()
def diary_read():
    last_time = datetime.datetime.now()
    while True:
        if (datetime.datetime.now() - last_time) > (datetime.timedelta(seconds=10)):
            print('прошло 10 секунд')
            last_time = datetime.datetime.now()
            file = open('diary.txt', 'r', encoding = 'utf-8')
            all_data = file.readline().split(':')
            if len(all_data) == 1:
                break
            date, message = all_data
            date_first = datetime.datetime.strptime(date, '%d %m %Y %H-%M').date()
            today = datetime.datetime.now().date()
            print(date, message)
            if date_first == today:
                print('Всплывающее сообщение')
                toaster.show_toast(f'Your diary!', message)
    file.close()
diary_read()
# 1. Сохраняем время в last_time.
# 2. Создаем цикл бесконечныйc
# 3. Если нынешнее время - last_time больше 1 минуты -> (datetime.timedelta(minutes=1)), то
#     - пишем "прошла 1 минута"
#     - обновляем last_time


