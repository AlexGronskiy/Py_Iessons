import random

print("Задание 1")
print(len(set(map(int, input('Введите целочисленные значения списка через пробел:').split()))))

print("Задание 2")
print(len(set(set(input('Введите целочисленные значения 1-го списка через пробел:').split()).union(set(input(
    'Введите целочисленные значения 2-го списка через пробел:').split())))))

print("Задание Д1")
magazines = 75  # int(input('Введите кол-во семей делающих журналы:'))
newspapers = 27  # int(input('Введите кол-во семей делающих газеты:'))
magazines_newspapers = 13  # int(input('Введите кол-во семей делающих журналы и газеты:'))
print("Живёт жителей в доме N:", magazines - magazines_newspapers + newspapers)

print("Задание Д2")
all_students = 52  # int(input('Введите кол-во учиников:'))
icons = 23  # int(input('Введите кол-во учиников собирающих значки:'))
stamps = 35  # int(input('Введите кол-во учиников собирающих марки:'))
icons_stamps = 16  # int(input('Введите кол-во учиников собирающих значки и марки:'))
print("Кол-во учеников ничем увлекающихся:", all_students - (icons - icons_stamps + stamps))

print("Задание Д3")
d_in_pl = 19  # int(input('Введите кол-во учиников:'))
d_in_c = 10  # int(input('Введите кол-во учиников:'))
d_in_s = 6  # int(input('Введите кол-во учиников:'))
d_in_pl_c = 5
d_in_pl_s = 3
d_id_c_s = 1
d_in_d = 3
print("Кол-во учеников в классе:", d_in_pl + d_in_c + d_in_s - (d_in_pl_c + d_in_pl_s + d_id_c_s) + 3)

print("Задание Д4")
n = 40
a = 25
b = 22
c = 22
ab = 33
ac = 32
bc = 31
abc = 10
one = ((ac - c - (b - (ab - a + abc))) + (ab - a - (c - (bc - b + abc))) + (bc - b - (a - (ac - c + abc))))
two = (b - (ab - a + abc)) + (c - (bc - b + abc)) + (a - (ac - c + abc))
zero = n - one - two - abc
print("Кол-во учеников прочитавших 1-у книгу:", one)
print("Кол-во учеников прочитавших 2-е книги:", two)
print("Кол-во учеников прочитавших 0 книг:", zero)
