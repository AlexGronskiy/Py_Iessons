print("Задание 1")
lst = list(map(int, input('Введите целочисленные значения списка через пробел:').split()))
k = int(input("Введите число - позицию элемента(0 - это первый элемент):"))
tmp = lst[k]
if k > 0:
    for k in range(k, len(lst) - 1):
        lst[k] = lst[k + 1]
lst[len(lst) - 1] = tmp
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
# print(len(set(set(input('Введите целочисленные значения 1-го списка через пробел:').split()) ^ set(input(
#    'Введите целочисленные значения 2-го списка через пробел:').split()))))
lst1 = list(map(int, input('Введите целочисленные значения 1-го списка через пробел:').split()))
lst2 = list(map(int, input('Введите целочисленные значения 2-го списка через пробел:').split()))
lst1.sort()
lst2.sort()
lst1 = list(map(int, input('Введите целочисленные значения 1-го списка через пробел:').split()))
lst2 = list(map(int, input('Введите целочисленные значения 2-го списка через пробел:').split()))
lst = []
for i in lst1:
    while lst1.count(i) > 1:
        lst1.remove(i)
for i in lst2:
    while lst2.count(i) > 1:
        lst2.remove(i)
lst1.sort()
lst2.sort()
for i in lst1:
    if i not in lst2:
        lst.append(i)
        continue
    for j in lst2:
        if j not in lst1:
            lst.append(j)
lst.sort()
print(lst)
print("В этих строках столько не пересекающихся символов:", len(lst))
