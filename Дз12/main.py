import random

n = int(input("Введите N для квадратной матрицы:"))
while True:
    if n > 5:
        Matrix = [[random.randint(1, 50) for j in range(n)] for i in range(n)]

        break
    else:
        print("Введите N > 5:")
        n = int(input("Введите N для квадратной матрицы:"))

print('Matrix:')
for row in Matrix:
    print(*map('{:>3d}'.format, row))
Matrix = list(map(list, zip(*Matrix)))
tmp_1 = [sum([abs(j) for j in Matrix[i]]) for i in range(n)]
print(list(tmp_1))


def sort(m):
    # сортировка столбцов по возростанию их сум
    k = 1
    while k < len(m):
        for i in range(len(m) - k):
            if tmp_1[i] > tmp_1[i + 1]:
                tmp_1[i], tmp_1[i + 1] = tmp_1[i + 1], tmp_1[i]
                Matrix[i], Matrix[i + 1] = Matrix[i + 1], Matrix[i]
        k += 1
    k = 1
    while k < len(m):
        for i in range(len(m)):
            for j in range(len(m) - 1):
                if i % 2:
                    if m[i][j] > m[i][j + 1]:  # сортировка методом пузырька
                        m[i][j], m[i][j + 1] = m[i][j + 1], m[i][j]
                else:
                    if m[i][j] < m[i][j + 1]:  # сортировка методом камушка
                        m[i][j], m[i][j + 1] = m[i][j + 1], m[i][j]
        k += 1

    lst = list(zip(*m))
    return lst


def print_new_matrix():
    print('New matrix:')
    for r in sort(Matrix):
        print(*map('{:>3d}'.format, r))
    print(tmp_1)


print_new_matrix()
