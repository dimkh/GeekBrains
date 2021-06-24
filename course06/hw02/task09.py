def sum_numbers(num: str) -> int:
    """ Суммирование цифр числа.
    На входе: натуральное число (задано строкой).
    На выходе: сумма цифр числа.
    """
    summa = 0
    num = int(num)
    while num != 0:
        summa += num % 10
        num //= 10
    return summa


# Формируем список исходных чисел
list_num = input('Введите натуральные числа (через пробел):').split()

max_sum = 0
for item in list_num:
    item_sum = sum_numbers(item)
    if max_sum < item_sum:
        max_sum = item_sum

print(f'Максимальная сумма цифр числа из списка {list_num} равна {max_sum}')
