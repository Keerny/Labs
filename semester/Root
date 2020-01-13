a = float(input('Введите число: '))
def koren (a):
    x = 3
    k = 0
    if (a<0):
        raise ValueError('Ошибка, введите число, меньшее нуля')
    while k != (a**0.5):
        k = 0.5 * (x + a/x)
        x = k
    return(k)
print('Корень из числа ' + str(a) + ' равен ' + str(koren(a)))
