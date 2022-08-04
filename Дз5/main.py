print("Задание 1")
a = int(input("Введите число:"))
k = a
while a > 0:
    b = a // 10
    c = a % 10
    a //= 10
    while b != 0:
        if c == b % 10:
            print(k)
            print('YES')
            break
        elif c != b % 10:
            b //= 10
    if b == 0:
        print(k)
        print('NO')
    break

print("Задание 2")
N = int(input("Введите число:"))
i = 1
count_2 = 0
while i <= N:
    t = i
    while t != 0:
        count_2 += 1
        t //= 10

    if i == ((i ** 2) % (10 ** count_2)):
        print(i, "*", i, "=", i ** 2)
    else:
        count_2 = 0
    i += 1

print("Задание 3")

su = 0
c = 0
c_p = 0
c_np = 0
minn = 0
maxx = 0
while True:
    n = int(input("Введите число:"))
    su += n
    c += 1

    if n == 0:
        break

    if n % 2 == 0:
        c_p += 1
    else:
        c_np += 1

    if n > maxx:
        maxx = n

    if n < minn or minn == 0:
        minn = n
print("Сумма чисел:", su)
print("Среднее арифметическое:", su / (c - 1))
print("Мин:", minn, "Макс:", maxx)
print("Парных:", c_p, "Не парных:", c_np)

print("Задание 4")
N = int(input("Введите число:"))
i = 1
print(N)
while i ** 2 <= N:
    print(i, "*", i, "=", i ** 21)
    i += 1
