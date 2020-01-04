import math
import json

print ('Дабы прекратить вычисление нажмите Ctrl+Z')
x1 = float(input('Введите ограничение: '))
x2 = float(input('Введите второе ограничение: '))
h = float(input('Введите шаг: '))
a = float(input('Введите переменную (а): '))
my_Glist = []
my_Flist = []
my_Ylist = []
if x1 > x2:
    x1,x2 = x2,x1
if h<0:
    h = -h
while x1 <= x2:
    if 15*a*a+29*a*x1+12*x1*x1 == 0:
        print('Деление на ноль')
    else:
        G = (4*(-18*a*a+3*a*x1+10*x1*x1))/(15*a*a+29*a*x1+12*x1*x1)
        my_Glist.extend([G])
    x1 = x1 + h
my_Gstring = str(my_Glist)




while x1 <= x2:
    F = math.tan(15*a*a-41*a*x1+28*x1*x1)
    my_Flist.extend([F])
    x1 = x1 + h
my_Fstring = str(my_Flist)




while x1 <= x2:
    if ((a*(-a)+3*a*x1+4*x1*x1+1)<-1) or ((a*(-a)+3*a*x1+4*x1*x1+1)>1):
        print ('Арккосинус не может быть этим значением')
    else:
        Y = math.acos(a*(-a)+3*a*x1+4*x1*x1+1)
        my_Ylist.extend([Y])
    x1 = x1 + h
my_Ystring = str(my_Ylist)

my_structure = []

my_structure = [my_Ystring, my_Fstring, my_Gstring]

h = int(input('Чтобы сохранить файл нажмите 1: '))
if h == 1:
    with open('file.txt', 'w') as fw:
        json.dump(my_structure, fw)
    my_structure = []
    
    l = int(input('Чтобы открыть файл нажмите 1: '))
    if l == 1:
        with open('file.txt', 'r') as fr:
        lst = json.load(fr)
        
else:
    print ('Файл не был сохранён')
