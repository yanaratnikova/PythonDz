print("Введите число: ")
n = int(input())
if n < 100 or n > 999:
    print("Это не трехзначное число. Повторите ввод.")
else:
    sum = 0
    while n // 10 > 0:
        sum = sum + n % 10
        n = n // 10
    sum = sum + n % 10
    print(f'сумма цифр в числе равна: {sum}')