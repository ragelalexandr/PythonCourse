# Пользователь вводит дату, а программа выдает ему день недели этой даты (нужно погуглить).

from datetime import datetime
#ПРОВЕРКА ФОРМАТА ДАТЫ!!!
# НАЗВАНИЕ ДНЕЙ НЕДЕЛИ В СПИСКЕ, ВЫБОР ПО ЧИСЛУ ДНЯ!!!
d = input("Введите дату в формате ddmmyyyy\n")
dw = (datetime.strptime(d, '%d%m%Y').isoweekday())
dwd = dict{'1': 'Понедельник', '2':'Вторник','3':'Среда','4':'Четверг','5':'Пятница','6':'Суббота','7':'Воскресенье'}
print(dwd)