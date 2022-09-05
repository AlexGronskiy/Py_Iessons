import random
print("Задание 1")
n = int(input("Введите длину строки:"))
k = int(input("Введите число(эквивалент суммы):"))


def list_gen(string_size, equivalent):
    st = [random.randint(-5, 5) for i in range(string_size)]
    for i in st:
        for j in reversed(st):
            if i + j != equivalent and i != st[-1]:
                next(reversed(st))
            elif i + j == equivalent:
                return True
            elif i == st[-1]:
                return False


print("Первый запрос:", list_gen(n, k))
print("Второй запрос:", list_gen(n, k), "\n")

print("Задание 2")
x_lst = [random.randint(-5, 5) for i in range(10)]
Y = int(input("Введите y(степень для x):"))
lst = map(lambda x, y: x**y, x_lst, [Y for j in range(len(x_lst))])
print(x_lst)
print(list(lst), "\n")

print("Задание 3")
# prime = [2] + [num for num in range(3, 101, 2) if all(num % i != 0 for i in range(2, int(math.sqrt(num))+1))]
# for num in range(2, 101):
#     if all(num % i != 0 for i in range(2, int(math.sqrt(num))+1)):


def primes(l):
    if l > 1:
        primes_found = [(2, 4)]
        yield 2
        for j in range(3, l, 2):
            for p, ps in primes_found:
                if ps > j:
                    primes_found.append((j, j * j))
                    yield j
                    break
                else:
                    if not j % p:
                        break


for i in primes(101):
    print(i, end=' ')
print("\n")

print("Задание 4")


def decor_table(func):
    def wrapper():
        print("╔═════════╦════════════╦══════════╗")
        func(st, multiplicity, pairing)

    return wrapper


def f_val_m(s):
    f_multiplicity = []
    for j in s:
        if j % 3 == 0:
            f_multiplicity.append("Кратно 3")
        else:
            f_multiplicity.append("Не кратно 3")
    return f_multiplicity


def f_val_p(s):
    f_pairing = []
    for k in s:
        if k % 2 == 0:
            f_pairing.append("Парное")
        else:
            f_pairing.append("Не парное")
    return f_pairing


@decor_table
def f_print(s, m, p):
    for i in range(len(s)):
        print("║" + '{:>8}'.format(s[i]) + ' ' + "║" + '{:<12}'.format(m[i]) + "║" + '{:<10}'.format(p[i]) + "║")
        if i != len(s)-1:
            print("╠═════════╬════════════╬══════════╣")
        else:
            print("╚═════════╩════════════╩══════════╝")


st = [random.randint(0, 100) for i in range(10)]
st.sort()
multiplicity = f_val_m(st)
pairing = f_val_p(st)
f_print()
# print(st)
# print(multiplicity)
# print(pairing)
# st, multiplicity, pairing