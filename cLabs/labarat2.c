#include <stdio.h>
#include <math.h>

int main(void)
{
float a,x,g,f,y;
int q;

printf ("Vvedite 1, 2 or 3: ");
scanf ("%i", &q);

switch (q)
{
case 1:
        printf("Vvedite x: ");
        scanf ("%f", &x);
        printf("Vvedite a: ");
        scanf ("%f", &a);
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
