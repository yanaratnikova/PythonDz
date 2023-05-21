# Требуется вывести все целые степени двойки 
# (т.е. числа вида 2k), не превосходящие числа N.

N = int(input('Введите число: '))

r = range(N)
for i in r:
    temp = 2**i
    if temp > N:
        break
    print(temp)