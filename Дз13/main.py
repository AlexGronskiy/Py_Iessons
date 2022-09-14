import random

n = int(input("Введите N для квадратной матрицы:"))
m = int(input("Введите M для квадратной матрицы:"))
Matrix = [[random.randint(1, 50) for j in range(n)] for i in range(m)]
print('Matrix:')


def sum_line(l):
    sum_l = 0
    for i in l:
        sum_l += i
    return sum_l


def sum_row(r):
    sum_r = 0
    for i in r:
        sum_r += i
    return sum_r


for row in Matrix:
    print(*map('{:>4d}'.format, row), *map('{:>7d}'.format, list([sum_line(row)])))
Matrix = list(map(list, zip(*Matrix)))
tmp_1 = [sum_row(j) for j in Matrix]
print(*map('{:>4d}'.format, tmp_1))