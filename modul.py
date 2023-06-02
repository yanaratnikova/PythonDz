# Сложение элементов
def sum_args(*args):
    res = 0
    for i in args:
        res += int(i)
    return res

# Возведение в степень с помощью рекурсии
def exponentiation(a, b):
    if b > 0:
        return a*exponentiation(a, b - 1)
    else:
        return 1
    
# Сумма двух чисел с помощью рекурсии    
def sum_nums(a, b):
    if b > 0:
        return 1 + sum_nums(a, b - 1)
    else:
        return a    