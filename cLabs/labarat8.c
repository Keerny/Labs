#include <stdio.h>
#include <math.h>
int main()
{
int i, n, c = 0;
float r, a, b, x, y;
printf("Введите общее количество точек: ");
scanf("%i", &n);

printf("Введите радиус: ");
scanf("%f", &r);

printf("Введите координаты центра окружности: ");
scanf("%f",&a);
scanf("%f",&b);

printf("Введите координаты точек: \n");

for (i = 0; i < n; i++)
{
    printf("x = ");
    scanf("%f",&x);
    printf("y = ");
    scanf("%f",&y);
    if (sqrt(x-a)+sqrt(y-b)<=sqrt(r))
    {
        c += 1;
    }
}
if (c == 0)
{
    printf("Ни одна точка не принадлежит окружности");
}
else
{
    printf("Количество точек, принадлежащих окружности: %i\n", c);
}
}
