# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданн

numbers = int(input('Введите число количество кустов: '))
new_dict_for = {}
for n in range(1, numbers + 1):
    new_dict_for[n] = n
print(new_dict_for)
i = int(input('Введите номер куста: '))
if i == numbers:
    new_dict_for[numbers+1] = new_dict_for[numbers] + 1
if i == 1:
    d1 = {0: numbers}
    new_dict_for, d1 = d1, new_dict_for
    new_dict_for.update(d1)
s = new_dict_for[i] + new_dict_for[i-1] + new_dict_for[i+1]
print(new_dict_for)
print(f"Количество ягод: {s}")