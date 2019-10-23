import math
print ('Vvedite 1, 2 or 3')
q=int(input())
if q==1:
        print ('Vvedite x')
        x=float(input())
        print ('Vvedite a')
        a=float(input())
        if 15*a*a+29*a*x+12*x*x!=0:
                print ('G=',(4*(-18*a*a+3*a*x+10*x*x))/(15*a*a+29*a*x+12*x*x))
        else:
                print ('Znachenie ne podhodit')

elif q==2:
        print ('Vvedite x')
        x=float(input())
        print ('Vvedite a')
        a=float(input())
        print ('F=',math.tan(15*a*a-41*a*x+28*x*x))

elif q==3:
        print ('Vvedite x')
        x=float(input())
        print ('Vvedite a')
        a=float(input())
        if (a*(-a)+3*a*x+4*x*x+1>=-1) and (a*(-a)+3*a*x+4*x*x+1<=1):
                print ('Y=',math.acos(a*(-a)+3*a*x+4*x*x+1))
        else:
                print ('Znachenie ne podhodit')
else:
        print ('Nepravilnoe znachenie')

