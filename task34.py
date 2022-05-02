# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
# нужно вытянуть из файлов уравнения и сложить их многочлены и прировнять к нулю
data = open('Annaeva.txt','r')
for line in data:                           
    n_str =line
data.close()
n_str=n_str.replace("=","").replace("0","")

data = open('Annaeva2.txt','r')
for line in data:
    n_str2 =line
data.close()
n_str2=n_str2.replace("=","").replace("0","")

result = n_str + '+' + n_str2 + '= ' + '0'

with open('Annaeva3.txt', 'w') as data:
   data.write(result)
print(result)