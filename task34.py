# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
# нужно вытянуть из файлов уравнения и сложить их многочлены и прировнять к нулю
data = open('Annaeva.txt','r')
for line in data:                           
    n_str =line
data.close()

first_coef=int(n_str[0]+n_str[1])
second_coef = int(n_str[10]+n_str[11])
three_coef = int(n_str[19]+n_str[20])

data = open('Annaeva2.txt','r')
for line in data:
    n_str2 =line
data.close()

first_coef2=int(n_str2[0]+n_str2[1])
second_coef2 = int(n_str2[10]+n_str2[11])
three_coef2 = int(n_str2[19]+n_str2[20])


first_coef = str(first_coef + first_coef2)
second_coef =str(second_coef + second_coef2)
three_coef =str(three_coef + three_coef2)

result = first_coef + '*x^2 ' + ' + ' + second_coef + '*x ' + ' + ' + three_coef + ' = 0'
with open('Annaeva3.txt', 'w') as data:
   data.write(result)
print(result)
