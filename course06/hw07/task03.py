import numpy as np

def sort_merge(ar: list) -> list:
    """ Сортировка массива по возрастанию методом слияния
    На входе: неотсортированный массив.
    На выходе: отсортированный массив по возрастанию (от меньшего к большему)
    """

    # Эту функцию вызываем рекурсивно до тех пор, пока не останутся массивы из 1 элемента
    if len(ar) < 2:
        return ar

    # Делим массив на 2 части
    middle_el = len(ar) // 2

    # Рекурсивно снова делим каждую часть на 2 части
    left_ar = sort_merge(ar[:middle_el])
    right_ar = sort_merge(ar[middle_el:])

    # Склеиваем 2 маленьких массива в 1 отсортированный
    return merge(left_ar, right_ar)


def merge(l_ar: list, r_ar: list) -> list:
    """ Склеивание двух маленьких массивов в один большой (отсортированный по возрастанию).
    На входе: два маленьких массива.
    На выходе: один большой отсортированный
    """
    res_ar = []         # В этот массив будут копироваться элементы по возрастанию
    i, j = 0, 0         # Индексы "первых элементов" левого и правого массивов

    while i < len(l_ar) and j < len(r_ar):          # Пока в массивах есть элементы - сравниваем их
        if l_ar[i] < r_ar[j]:
            res_ar.append(l_ar[i])
            i += 1
        else:
            res_ar.append(r_ar[j])
            j += 1

    # Один из массивов закончился - добавляем в результат остатки другого
    while i < len(l_ar):
        res_ar.append(l_ar[i])
        i += 1
    while j < len(r_ar):
        res_ar.append(r_ar[j])
        j += 1

    return res_ar


count_elem = 10

# Генерируем тестовый массив из count_elem элементов заданного диапазона
array = np.random.uniform(0, 50, count_elem)

# Для удобства округляем до сотых
_round = lambda x: round(x, 2)
array = ([_round(num) for num in array])

print(f'\nИсходный массив из {count_elem} элементов:')
print(array)

print(f'\nОтсортированный по возрастанию массив:')
print(sort_merge(array), '\n')
