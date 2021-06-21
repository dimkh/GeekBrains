import random as rnd

# Генерируем исходный массив натуральных чисел
count_elem = 10
max_elem = 10
nat_lst = [rnd.randint(1, max_elem) for _ in range(count_elem)]
print(f'Исходный массив из {count_elem} чисел: {nat_lst}')

# Для min и max элементов находим первые вхождения в список (т.е. дубли не учитываю)
min_elem = min(nat_lst)
min_elem_idx = nat_lst.index(min_elem)
max_elem = max(nat_lst)
max_elem_idx = nat_lst.index(max_elem)
print(f'min число {min_elem} с индексом {min_elem_idx}')
print(f'max число {max_elem} с индексом {max_elem_idx}')

if min_elem_idx > max_elem_idx:
    max_elem_idx, min_elem_idx = min_elem_idx, max_elem_idx

# Находим сумму чисел между min и max числами
sum_result = 0
for i in range(min_elem_idx + 1, max_elem_idx):
    sum_result += nat_lst[i]

print(f'Сумма чисел между max и min числами равна {sum_result}')