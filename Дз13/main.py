import random

n = int(input("Введите N (кол-во столбцов) матрицы:"))
m = int(input("Введите M (кол-во строк) матрицы:"))
Matrix = [[random.randint(1, 50) for j in range(n)] for i in range(m)]
print('Matrix:')


def sums(l):
    sum_l = 0
    for i in l:
        sum_l += i
    return sum_l


for row in Matrix:
    print(*map('{:>4d}'.format, row), *map('{:>7d}'.format, list([sums(row)])))
Matrix = list(map(list, zip(*Matrix)))
tmp_1 = [sums(j) for j in Matrix]
print(*map('{:>4d}'.format, tmp_1))