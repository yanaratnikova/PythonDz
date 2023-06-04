#  Определить индексы элементов массива (списка), значения которых 
# принадлежат заданному диапазону (т.е. не меньше заданного минимума 
# и не больше заданного максимума
import random
items = [random.randint(0, 10) for i in range(15)]
print(items)
min_ = int(input('Укажите диапозон. От: '))
max_ = int(input('До: '))
for i in range(len(items)):
    if min_ < items[i] < max_:
        print(i)