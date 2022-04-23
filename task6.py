# Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.
number = int(input('Введите число от 1 до 7:'))
while number > 7 or number < 1:
    if number > 7 or number < 1:
        print('Введите число ещё раз:', end =' ')
        number = int(input())
    if number == 1: print('Понедельник - будний день')
    elif number == 2: print('Вторник - будний день')
    elif number == 3: print('Среда - будний день')
    elif number == 4: print('Четверг - будний день')
    elif number == 5: print('Пятница - будний день')
    elif number == 6: print('Суббота - выходной день')
    elif number == 7: print('Воскресенье - выходной день')
