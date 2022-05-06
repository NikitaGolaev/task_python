# Подсчитать сумму цифр в вещественном числе
n =input('Введите число: ')
length = len(n)
n = int(n)
sum = 0
for i in range(length):
    sum = sum + (n %10)
    n=n//10
    i += i
print(sum)

