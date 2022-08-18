print("Задание 1")
lst = list(map(int, input('Введите целочисленные значения списка через пробел:').split()))
k = int(input("Введите число - сдвиг:"))

for i in range(abs(k)):
    if k < 0:
        lst = lst[1:] + lst[:1]
    elif k > 0:
        lst = lst[-1:] + lst[:-1]
    else:
        break
lst.pop()
print(lst)

print("Задание 2")
lst = list(map(int, input('Введите целочисленные значения списка через пробел:').split()))
k = int(input("Введите число - позицию элемента(0 - это первый элемент):"))
a = int(input("Введите число - вставеу:"))
lst.append(a)
for k in range(k, len(lst)):
    lst[-1], lst[k] = lst[k], lst[-1]
    k += 1
print(lst)

print("Задание 3")
print(len(set(set(input('Введите целочисленные значения 1-го списка через пробел:').split()) ^ set(input(
    'Введите целочисленные значения 2-го списка через пробел:').split()))))
