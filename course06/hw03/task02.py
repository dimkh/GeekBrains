import random as rnd

# Генерируем исходный массив натуральных чисел
count_elem = 10
max_elem = 100
nat_lst = [rnd.randint(1, max_elem) for _ in range(count_elem)]

res_lst = list()
for i in range(count_elem):
    # Четное число - сохраняем индекс
    if nat_lst[i] % 2 == 0:
        res_lst.append(i)

print(f'Исходный массив: {nat_lst}')
print(f'Четные элементы: {res_lst}')
