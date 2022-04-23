# Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У 
while True:
    try:
        x = input('Введите x = ')
        y = input('Введите y = ')
        x, y = int(x), int(y)  
        if x > 0 < y: 
            print('Точка находится во II четверти координатной плоскости')
            break
        elif x > 0 < y: 
            print('Точка находится во III четверти координатной плоскости')
            break
        elif x < 0 < y: 
            print('Точка находится во IV четверти координатной плоскости')
            break
        elif x < 0 > y: 
            print('Точка находится во I четверти координатной плоскости')
            break
        elif x == 0 == y: 
            print('Точка начала координат')
            break
        elif x == 0:
            print('Точка находится на оси y')
            break
        elif y == 0:
            print('Точка начходится на оси x')
            break
        else:
            raise ValueError
    except ValueError:
        continue