import random

print("Задание 1")
dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}
dictionary_1.update(dictionary_2)
print(dictionary_1)

print("Задание 2")
dictionary = {i: random.randint(1, 11) for i in range(20)}
print(dictionary)
result = 1
for key in dictionary:
    result = result * dictionary[key]
print("Результат умножения:", result)

print("Задание 3")
dictionary = {i + 1: (i + 1)**3 for i in range(10)}
print(dictionary)

print("Задание 4")
keys = [random.randint(-5, 5) for i in range(5)]
values = [random.randint(-5, 5) for i in range(5)]
print("1-ый список", keys)
print("2-ой список", values)
# dictionary = {i: i for i in zip(dictionary_1, dictionary_2)}
dictionary = dict(zip(keys, values))
print("Созданный словарь:", dictionary)

print("Задание 5")
s = 'pythonist'
my_dict = {i: s.count(i) for i in s}
print(my_dict)

print("Задание 6")
S = """Любіть Україну, як сонце любіть,
як вітер, і трави, і води...
В годину щасливу і в радості мить,
любіть у годину негоди.

Любіть Україну у сні й наяву,
вишневу свою Україну,
красу її, вічно живу і нову,
і мову її солов'їну.

Без неї - ніщо ми, як порох і дим,
розвіяний в полі вітрами...
Любіть Україну всім серцем своїм
і всіми своїми ділами.""".lower()
S = S.lower().replace(',', '').replace('.', '').replace(' -', '').split()
dictionary = {word: S.count(word) for word in set(S)}
print("Словарь (слово: кол-во):\n", dictionary)
