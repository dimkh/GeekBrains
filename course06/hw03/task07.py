import random as rnd

# Генерируем исходный массив натуральных чисел
count_elem = 10
max_elem = 10
nat_lst = [rnd.randint(1, max_elem) for _ in range(count_elem)]
print(f'Исходный массив из {count_elem} чисел: {nat_lst}')

min_elem1 = min(nat_lst)
nat_lst.remove(min_elem1)
min_elem2 = min(nat_lst)

print(f'Два минимальных числа списка: {min_elem1} и {min_elem2}')
