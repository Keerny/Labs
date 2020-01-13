#include <stdio.h>
#include <math.h>

int main(void)
{
float a,x1,x2,h,g,f,y;
int q;

printf("Введите первую границу: ");
scanf ("%f", &x1);
printf("Введите вторую границу: ");
scanf ("%f", &x2);
printf("Введите переменную а: ");
scanf ("%f", &a);
printf("Введите шаг: ");
scanf ("%f", &h);
printf ("Выберите 1ю, 2ю, или 3ю функцию: ");
scanf ("%i", &q);

switch (q)
{
case 1:
        if (15*a*a+29*a*x+12*x*x!=0)
        {
                g=4*(-18*a*a+3*a*x+10*x*x)/(15*a*a+29*a*x+12*x*x);
                printf("g = %f\n\n", g);
        }
        else
        {
                printf ("%s\n", "Znachenie ne podhodit");
        }
        break;

case 2:
        printf("Vvedite x ");
        scanf ("%f", &x);
        printf("Vvedite a ");
        scanf ("%f", &a);
        f=tan(15*a*a-41*a*x+28*x*x);
        printf("f=%f\n\n", f);
        break;

case 3:
        printf("Vvedite x ");
        scanf ("%f", &x);
        printf("Vvedite a ");
        scanf ("%f", &a);
        if (-1*a*a+3*a*x+4*x*x+1 >= -1 && -1*a*a+3*a*x+4*x*x+1 <= 1)
        {
                y=acos(-1*a*a+3*a*x+4*x*x+1);
                printf("y=%f\n\n", y);
        }
        else
        {
                printf ("Znachenie ne podhodit");
        }
        break;
default:
        printf("%s\n", "Error: wrong function.");
}

return 0;
}
