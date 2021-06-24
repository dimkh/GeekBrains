import cProfile

def sum_series(el: int) -> float:
    """ Вычисление суммы ряда через цикл для оценки производительности.
    На входе: количество элементов ряда для суммирования.
    На выходе: Сумма ряда.
    """

    sum_el = 0
    element = 1
    for i in range(el):
        sum_el +=  element
        element *= -0.5

    return sum_el


def main(count: int) -> float:
    """ Многократное вычисление суммы ряда через цикл для оценки производительности.
    На входе: количество повторов вычислений.
    На выходе: Сумма ряда.
    """
    for i in range(count):
        res = sum_series(990)
    print(res)

    return res


cProfile.run('main(1000)')
