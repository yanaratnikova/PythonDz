# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a1 = int(input('Первый элемент арифметической прогрессии: '))
n = int(input('Количество элементов: '))
d = int(input('Разность: '))
a = []
for i in range(1, n + 1):
    a_ = a1 + (i - 1)*d
    a.append(a_)
print(a)