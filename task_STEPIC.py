num_1 = int(input())
letter_1 = input()
num_2 = int(input())
letter_2 = input()

def examination (num, letter):
    if num % 2 == 0 and (letter =='b' or letter =='d' or letter =='f' or letter =='h'):
        color ='черный'
    elif num % 2 == 0 and (letter =='a' or letter =='c' or letter =='e' or letter =='g'):
        color ='белый'
    elif num % 2 != 0 and (letter =='b' or letter =='d' or letter =='f' or letter =='h'):
        color ='черный'
    elif num % 2 != 0 and (letter =='a' or letter =='c' or letter =='e' or letter =='g'):
        color ='белый'
    print(color)
    return color
color_1 = examination(num_1,letter_1)
color_2 = examination(num_2,letter_2)
if color_1 == color_2:
    print('YES')
else:print('NO')