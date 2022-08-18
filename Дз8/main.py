import random

print("Задание 1")
n = int(input("Введите N для квадратной матрицы:"))
a = []
for i in range(n):
    a.append([0] * n)
for i in range(n):
    t = n
    for j in range(n):
        if i % 2 != 0:
            a[i][j] = -t
            t -= 1
        else:
            a[i][j] = i
        print((int(a[i][j])),
              end=" " if j < n - 1 else '\n')

print("Задание 2")
n = int(input("Введите N для квадратной матрицы:"))
a = []
d_sum = 0
n_sum = 0
for i in range(n):
    a.append([0] * n)
for i in range(n):
    for j in range(n):
        a[i][j] = random.randint(-5, 5)
        if i == j:
            d_sum += a[i][j]
        n_sum += a[i][n-1]
        print((int(a[i][j])),
              end=" " if j < n - 1 else '\n')
print("Сумма диагональных элементов:", d_sum)
print("Сумма последних элементов строк:", n_sum)

print("Задание 3")
lst = []
sum_p = 0
sum_np = 0
for i in range(15):
    lst.append(15)
    lst[i] = random.randint(-5, 5)
    if lst[i] % 2 == 0:
        sum_p += lst[i]
    else:
        sum_np += lst[i]
print(lst)
if sum_np > sum_p:
    print("Да")
else:
    print("Нет")
