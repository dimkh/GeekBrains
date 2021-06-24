import random as rnd


def sum_nat(end_num: int) -> int:
    """ Сложение натуральных чисел от 1 до заданного.
    На входе: конечное число.
    На выходе: сумма чисел от 1 до конечного.
    Используется рекурсия.
    """

    # Для проверки печать на каждом проходе
    # print(end_num)

    if end_num == 1:
        return 1
    return end_num + sum_nat(end_num - 1)


# Задаём случайное число в диапазоне от 2 до 20
num = rnd.randint(2, 20)
sum_recur = sum_nat(num)
sum_form = int(num * (num + 1) / 2)

print(f'Сумма чисел от 1 до {num} (через рекурсию) равна {sum_recur}')
print(f'Сумма чисел от 1 до {num} (через формулу) равна {sum_form}')
if sum_recur == sum_form:
    print('Результат совпадает!')
else:
    print('Результат через рекурсию отличается от результата через формулу!!!')
