import random as rnd
import sys

# Генерируем исходный массив натуральных чисел
count_elem = 20
max_elem = 10
nat_lst = [rnd.randint(1, max_elem) for _ in range(count_elem)]
print(f'Исходный массив из {count_elem} чисел: {nat_lst}')

# Находим уникальные элементы списка
uniq_elem = set(nat_lst)

# Находим количество вхождений элементов
dict_elem = {}
for elem in uniq_elem:
    dict_elem[elem] = nat_lst.count(elem)
max_value = max(dict_elem.values())

if max_value == 1:
    print('Все значения списка уникальны!')
    sys.exit()

# Находим число, которое встречается чаще всего
# Если таких чисел несколько - выводим все
result = {}
for elem in dict_elem:
    if dict_elem[elem] == max_value:
        result[elem] = max_value

print(f'Количество вхождений: {dict_elem}')
print(f'Максимальная частота: {max_value}')
print(f'Самое частое число - количество вхождений: {result}')
