# Вывести на экран числа от -N до N
print('Введите число:', end='')
n = int(input())
n = abs(n)
for i in range (-n, n + 1):
    print(i, end = ' ')
