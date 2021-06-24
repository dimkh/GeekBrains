import random as rnd

# Генерируем исходный массив натуральных чисел
count_elem = 10
max_elem = 100
nat_lst = [rnd.randint(1, max_elem) for _ in range(count_elem)]

# Определяем значение max и min элементов и их индексы
# (первое вхождение в список, возможные повторы не учитываем)
min_elem = min(nat_lst)
min_elem_idx = nat_lst.index(min_elem)
max_elem = max(nat_lst)
max_elem_idx = nat_lst.index(max_elem)

print(f'Исходный массив: {nat_lst}')
print(f'Минимальное значение: {min_elem}, с индексом {min_elem_idx}')
print(f'Максимальное значение: {max_elem}, с индексом {max_elem_idx}')
print()

# Меняем min и max элементы местами
nat_lst[min_elem_idx], nat_lst[max_elem_idx] = nat_lst[max_elem_idx], nat_lst[min_elem_idx]

print(f'Поменяли местами max и min элементы: {nat_lst}')
