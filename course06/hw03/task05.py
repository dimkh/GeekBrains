import random as rnd

# Генерируем исходный массив натуральных чисел
count_elem = 10
max_elem = 10
nat_lst = [rnd.randint(-max_elem, max_elem) for _ in range(count_elem)]
print(f'Исходный массив из {count_elem} чисел: {nat_lst}')

index = -1
for i in range(count_elem):
    if nat_lst[i] < 0 and index == -1:
        index = i
    elif nat_lst[i] < 0 and nat_lst[i] > nat_lst[index]:
        index = i

if index == -1:
    print('Отрицательных чисел в списке нет!')
else:
    print(f'Максимальное отрицательное число: {nat_lst[index]}, его индекс равен {index}')
