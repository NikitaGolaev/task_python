# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
def examination (x, y, z):
    if not(x or y or z) == (not x and not y and not z):
        print(True)
    else: print(False)
if(examination(0,0,0)==examination(0,0,1)==examination(0,1,0)
==examination(1,0,0)==examination(0,1,1)==examination(1,1,0)
==examination(1,0,1)==examination(1,1,1)) == True:
    print('Утверждение истина')
else: print(False)
