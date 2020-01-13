import math
import random
import time

c = 0
n = int(input('Введите общее количество точек = '))
r = float(input('Введите радиус = '))
a = 0
b = 0
start_time = time.time()
for i in range(1, n+1):
    x = random.uniform(0, 100)
    y = random.uniform(0, 100)
    if math.sqrt(x-a)+math.sqrt(y-b)<=math.sqrt(r):
        c += 1
    print(time.time() - start_time) 
if c == 0:
    print('Ни одна точка не принадлежит окружности')
else:
    print('Количество точек, принадлежащих окружности: ', c)
