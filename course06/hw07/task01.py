import numpy as np

def sort_bubble(ar: list) -> list:
    """ Сортировка массива по возрастанию методом "пузырька"
    На входе: неотсортированный массив.
    На выходе: отсортированный массив по возрастанию (от меньшего к большему)
    """

    for i in range (count_elem - 1):
        for j in range (count_elem - i - 1):
            # Текущий элемент больше следующего - меняем их местами
            if ar[j] > ar[j + 1]:
                ar[j], ar[j + 1] = ar[j + 1], ar[j]

    return ar


count_elem = 10

# Генерируем тестовый массив из count_elem элементов заданного диапазона
array = np.random.randint(-100, 100, count_elem)

print(f'\nИсходный массив из {count_elem} элементов:')
print(array)
print(f'\nОтсортированный по возрастанию массив:')
print(sort_bubble(array), '\n')
