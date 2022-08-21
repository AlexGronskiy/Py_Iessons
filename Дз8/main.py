import random

print("Задание 1")
n = int(input("Введите N для квадратной матрицы:"))
a = [[i if i % 2 == 0 else (-n + j) for j in range(n)] for i in range(n)]
for i in range(n):
    print(a[i])

print("Задание 2")
n = int(input("Введите N для квадратной матрицы:"))
d_sum = 0
n_sum = 0
Matrix = [[random.randint(1, 11) for j in range(n)] for i in range(n)]
d_sum = [
    d_sum + Matrix[i][j]
    for j in range(n)
    for i in range(n)
    if i == j
]
n_sum = [
    n_sum + Matrix[i][j]
    for j in range(n)
    for i in range(n)
    if j == n - 1

]
print('Matrix:')
for i in range(n):
    print(Matrix[i])
print("Сумма диагональных элементов:", sum(d_sum))
print("Сумма последних элементов строк:", sum(n_sum))

print("Задание 3")
lst = [random.randint(-5, 5) for i in range(5)]
sum_p = 0
sum_np = 0
sum_p = [
    sum_p + i
    for i in lst
    if i % 2 == 0
]
sum_np = [
    sum_np + i
    for i in lst
    if i % 2 != 0
]
print(lst)
if sum(sum_np) > sum(sum_p):
    print(sum_np, '\n', "Да", sum(sum_np))
else:
    print(sum_p, '\n', "Нет", sum(sum_p))
