import math

print ('Дабы прекратить вычисление нажмите Ctrl+Z')
q = int(input('Выберите 1-ю, 2-ю или 3-ю функцию: '))
x1 = float(input('Введите ограничение: '))
x2 = float(input('Введите второе ограничение: '))
h = float(input('Введите шаг: '))
a = float(input('Введите переменную (а): '))
if x1 > x2:
    x1,x2 = x2,x1
if h<0:
    h = -h
if q == 1:
    while x1 <= x2:
        if 15*a*a+29*a*x1+12*x1*x1 == 0:
            print('Деление на ноль')
        else:
            print('{}; {}'.format(x1, (4*(-18*a*a+3*a*x1+10*x1*x1))/(15*a*a+29*a*x1+12*x1*x1)))
        x1 = x1 + h

elif q == 2:
    while x1 <= x2:
        print ('{}; {}'.format(x1, (math.tan(15*a*a-41*a*x1+28*x1*x1))))
        x1 = x1 + h

elif q == 3:
    while x1 <= x2:
        if ((a*(-a)+3*a*x1+4*x1*x1+1)<-1) or ((a*(-a)+3*a*x1+4*x1*x1+1)>1):
            print ('Арккосинус не может быть этим значением')
        else:
            print ('{}; {}'.format(x1, (math.acos(a*(-a)+3*a*x1+4*x1*x1+1))))
        x1 = x1 + h

else:
    print ('Такой функции не существует')

