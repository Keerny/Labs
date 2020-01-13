import math

c = 0
n = int(input('Введите общее количество точек = '))
r = float(input('Введите радиус = '))
print('Введите координаты центра окружности')
a = float(input())
b = float(input())
for i in range(1, n+1):
    print('Введите координаты ',i,' точки')
    x = float(input())
    y = float(input())
    if math.sqrt(x-a)+math.sqrt(y-b)<=math.sqrt(r):
        c += 1
if c == 0:
    print('Ни одна точка не принадлежит окружности')
else:
    print('Количество точек, принадлежащих окружности: ', c)
