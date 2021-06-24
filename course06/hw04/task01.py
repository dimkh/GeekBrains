import cProfile

def sum_series(n: int, first_elem: float) -> float:
    """ Вычисление суммы n первых элементов последовательности
    На входе: количество элементов для суммирования и первый элемент последовательности
    На выходе: сумма элементов.
    Используется рекурсия.
    """
    result = first_elem

    if n > 1:
        result += sum_series(n - 1, first_elem * (-0.5))
    return result


def main(count: int) -> float:
    """ Многократное вычисление суммы ряда через рекурсию для оценки производительности.
    На входе: количество повторов вычислений.
    На выходе: Сумма ряда.
    """
    for i in range(count):
        res = sum_series(990, 1)
    print(res)

    return res

cProfile.run('main(1000)')
