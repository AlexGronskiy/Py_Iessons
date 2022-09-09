import random

n = int(input("Введите N для квадратной матрицы:"))
while True:
    if n > 2:
        Matrix = [[random.randint(1, 5) for j in range(n)] for i in range(n)]

        break
    else:
        print("Введите N > 5:")
        n = int(input("Введите N для квадратной матрицы:"))

print('Matrix:')
for row in Matrix:
    print(*map('{:>3d}'.format, row))
Matrix = list(map(list, zip(*Matrix)))
tmp_1 = [sum([abs(j) for j in Matrix[i]]) for i in range(n)]
print(tmp_1)
print()

# сортировка столбцов по возростанию их сум
k = 1
while k < len(Matrix):
    for i in range(len(Matrix) - k):
        if tmp_1[i] > tmp_1[i + 1]:
            tmp_1[i], tmp_1[i + 1] = tmp_1[i + 1], tmp_1[i]
            Matrix[i], Matrix[i + 1] = Matrix[i + 1], Matrix[i]
    k += 1

# сортировка бульбошкой
for i in range(len(Matrix)):
    for j in range(len(Matrix) - 1):
        if Matrix[i][j] > Matrix[i][j + 1]:
            Matrix[i][j], Matrix[i][j + 1] = Matrix[i][j + 1], Matrix[i][j]
    print(Matrix[i])
print()
lst = list(zip(*Matrix))


print('Matrix:')
for row in lst:
    print(*map('{:>3d}'.format, row))
print(tmp_1)
