# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко 
#он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть,
# если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они
# разделяются дефисами. Фразы отделяются друг от друга пробелами.
#Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
#В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, 
#если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  
sogl = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п','р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']
#str = input()
str = 'Хорошо-живет-на-свете-Винни-Пух!'
str = str.lower()
str = list(str)
res = [element for element in str if element not in sogl]
for ele in res:
    if ele == '-':
        res.remove(ele)
res = ''.join(res)
res = res.split()
count = 0
p = res[0]
for i in res:
    if i != p:
        count += 1
    else:
        count += 0
if count == 0:
    print('Парам пам-пам')
else:
    print('Пам парам')