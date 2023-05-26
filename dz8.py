import random
n = int(input('Введите число элементов: '))
a = int(input('Введите искомое число: '))
count = 0
rand_list = []
for i in range(n):
    rand_list.append(random.randint(0, 10))
    if rand_list[i] == a:
        count = count + 1
print(rand_list)
print(f"Число {a} встречается {count} раза")