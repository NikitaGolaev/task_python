# Вычислить число c заданной точностью d 
# при 𝑑 = 0.001,𝜋 = 3.141 10−1≤𝑑≤10−10
import math
print ( math.pi )
d = float(input('Введите число в диапазоне от 0.1 до 0.0000000001: '))
def get_count(d):
    s = str(d)
    if '.' in s:
        return abs(s.find('.') -len(s)) -1
    else:
        return 0
count = get_count(d)
print(round(math.pi,count))


