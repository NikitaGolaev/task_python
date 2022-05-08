# Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
from dataclasses import replace

n = int(input('Введите число для последовательности списка: '))
li = [x for x in range(-n,n+1)]
print(li)

with open('file.txt','w') as data:
    data.write('0\n')
    data.write('1\n')

path = 'file.txt'
data = open(path,'r')
res = 1
for line in data:
    number = line.replace('\n','')
    number = int(number)
    num_1 = li[number]
    res = res*num_1
print('Произведение элементов на указанных позициях =', res)
data.close()