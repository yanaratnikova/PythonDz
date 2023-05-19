print('Введите номер билета:')
list_1 = list() 
for i in range(6): 
 n = int(input()) 
 list_1.append(n) 

print(list_1) 
if (list_1[0] + list_1[1] + list_1[2]) == (list_1[3] + list_1[4] + list_1[5]):
    print('Это счастливый билет!')
else:
    print('Билет как билет... ничего особенного')
