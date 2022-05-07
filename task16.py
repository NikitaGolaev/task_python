# Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму
n = int(input('Введите число: '))
li =[x for x in range(1,n)]
print(li)
li=list(map(lambda x:(x,((1+1/x)**x)),li))
print(li)
