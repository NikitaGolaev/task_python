# Найти расстояние между двумя точками пространства
from cmath import sqrt
import math

dot_1=(int(input('Введите значение x: ')),int(input('Введите значение y: ')),int(input('Введите значение z: ')))
print('Координаты 1 точки:', dot_1)
dot_2=(int(input('Введите значение x: ')),int(input('Введите значение y: ')),int(input('Введите значение z: ')))
print('Координаты 2 точки:', dot_1)
print('Расстояние между двумя точками:', end = '')
print(math.sqrt(math.pow((dot_2[0] - dot_1[0]),2) +
 math.pow((dot_2[1] - dot_1[1]),2) + 
 math.pow((dot_2[2] - dot_1[2]),2)))

