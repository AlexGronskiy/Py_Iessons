# import ag_sorts
import random
from ag_sorts import *  # __all__ = ["bubble_sort", "quick_sort", "insertion_sort"]

random_list_of_nums = [random.randint(1, 50) for j in range(10)]
r = random_list_of_nums
print(*map('{:>3d}'.format, r))
print("\n")
# ag_sorts.bubble_sort(r)
bubble_sort(r)
print(*map('{:>3d}'.format, r))
# ag_sorts.quick_sort(r)
quick_sort(r)
print(*map('{:>3d}'.format, r))
# ag_sorts.insertion_sort(r)
insertion_sort(r)
print(*map('{:>3d}'.format, r))
print("----------------------------------------------------------")
# print(help(ag_sorts))
print("----------------------------------------------------------")
print(dir())