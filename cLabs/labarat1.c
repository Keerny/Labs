#include <stdio.h>
#include <stdio.h>
#include <math.h>
int main(void)
{
float a,x,g,f,y;
printf("Vvedite x: ");
scanf ("%f", &x);
printf("Vvedite a ");
scanf ("%f", &a);
g=4*(-18*a*a+3*a*x+10*x*x)/(15*a*a+29*a*x+12*x*x);
printf("g=%f\n\n", g);

printf("Vvedite x ");
scanf ("%f", &x);
printf("Vvedite a ");
scanf ("%f", &a);
f=tan(15*a*a-41*a*x+28*x*x);
printf("f=%f\n\n", f);

printf("Vvedite x ");
scanf ("%f", &x);
printf("Vvedite a ");
scanf ("%f", &a);
y=acos(-1*a*a+3*a*x+4*x*x+1);
printf("y=%f\n\n", y);
}
