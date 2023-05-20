print("Введите ширину шоколадки: ", end='', flush=True)
n = int(input())
print("Введите длинну шоколадки: ", end='', flush=True)
m = int(input())
print("Введите количество долек в одном кусочке: ", end='', flush=True)
k = int(input())
for i in range(1, m + 1, 1):
    s = i * n
    if s == k:
        print("yes")
        break
else:    
    for i in range(1, n + 1, 1):
        s = i * m
        if s == k:
            print("yes")
            break
    else:        
        print("No")
