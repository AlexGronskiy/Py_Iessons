print("Задание 1")
n = int(input("Введите кол-во школьников:"))
k = int(input("Введите кол-во яблоко:"))
print("Каждый школьник получил по:", k // n)
print("В корзине осталось:", k % n)

print("Задание 2")
k1 = int(input("Введите кол-во школьников в 1-ой параллеле:"))
k2 = int(input("Введите кол-во школьников во 2-ой параллеле:"))
k3 = int(input("Введите кол-во школьников в 3-ой параллеле:"))
print("Для класса 1-ой параллели необходимо докупить:", k1 // 2 + k1 % 2)
print("Для класса 2-ой параллели необходимо докупить:", k2 // 2 + k2 % 2)
print("Для класса 3-ой параллели необходимо докупить:", k3 // 2 + k3 % 2)

print("Задание 3")
password = input("Введите пароль:")  # можно сделать статичным или же считывать из файла
log_password = input("Введите пароль:")
if log_password == password:
    print("Пароль верный!")
else:
    print("Пароль не верный!")

print("Задание 4")
year = int(input("Введите год:"))
if (year > 1900) and (year < 1000000):
    if year % 100 == 0 and year % 400 != 0:
        print(year, "is not leep year")
    elif year % 4 == 0 or year % 400 == 0:
        print(year, "is leep year")
    else:
        print(year, "is not leep year")
else:
    print(year, "is not in range 1900 < year < 1000000")
