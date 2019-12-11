import math

print ('Дабы прекратить вычисление нажмите Ctrl+Z')
q = int(input('Выберите 1-ю, 2-ю или 3-ю функцию: '))
x1 = float(input('Введите ограничение: '))
x2 = float(input('Введите второе ограничение: '))
h = float(input('Введите шаг: '))
a = float(input('Введите переменную (а): '))
my_list = []
if x1 > x2:
    x1,x2 = x2,x1
if h<0:
    h = -h
if q == 1:
    print (x1, (4*(-18*a*a+3*a*x1+10*x1*x1))/(15*a*a+29*a*x1+12*x1*x1))
    while x1 <= x2:
        if 15*a*a+29*a*x1+12*x1*x1 == 0:
            print('Деление на ноль')
        else:
            G = (4*(-18*a*a+3*a*x1+10*x1*x1))/(15*a*a+29*a*x1+12*x1*x1)
            my_list.extend([G])
        x1 = x1 + h
    print (x1, F)
        
elif q == 2:
    print (x1, math.tan(15*a*a-41*a*x1+28*x1*x1))
    while x1 <= x2:
        F = math.tan(15*a*a-41*a*x1+28*x1*x1)
        my_list.extend([F])
        x1 = x1 + h
    print (x1, F)

elif q == 3:
    print (x1, math.acos(a*(-a)+3*a*x1+4*x1*x1+1))
    while x1 <= x2:
        if ((a*(-a)+3*a*x1+4*x1*x1+1)<-1) or ((a*(-a)+3*a*x1+4*x1*x1+1)>1):
            print ('Арккосинус не может быть этим значением')
        else:
            Y = math.acos(a*(-a)+3*a*x1+4*x1*x1+1)
            my_list.extend([Y])
        x1 = x1 + h
    print (x1, Y)


else:
    print ('Такой функции не существует')
