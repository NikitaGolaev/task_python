# Найти максимальное из пяти чисел
number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))
number3 = int(input('Введите третье число: '))
number4 = int(input('Введите четвертое число: '))
number5 = int(input('Введите пятое число: '))
max = number1

if max < number2: max = number2
if max < number3: max = number3
if max < number4: max = number4
if max < number5: max = number5
print('Максимальное число = ', end = '')
print(max)