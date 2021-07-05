def add_hex(n1: list, n2: list) -> list:
    """ Сложение двух шестнадцатиричных чисел, хранящихся в формате ['A', '2'].
    На входе: 2 числа в формате списков.
    На выходе: результат сложения в формате списка.
    """

    number1 = int(''.join(n1), 16)
    number2 = int(''.join(n2), 16)
    number_sum = number1 + number2

    return list(hex(number_sum)[2:].upper())


def mul_hex(n1: list, n2: list) -> list:
    """ Перемножение двух шестнадцатиричных чисел, хранящихся в формате ['A', '2'].
    На входе: 2 числа в формате списков.
    На выходе: результат сложения в формате списка.
    """

    number1 = int(''.join(n1), 16)
    number2 = int(''.join(n2), 16)
    number_sum = number1 * number2

    return list(hex(number_sum)[2:].upper())


num1 = input('Ввведите первое шестнадцатиричное число: ')
num2 = input('Ввведите второе шестнадцатиричное число: ')

num1_l = list(num1)
num2_l = list(num2)

print('\nВведены числа:')
print(num1_l)
print(num2_l)

print(f'\nРезультат сложения двух чисел: {add_hex(num1_l, num2_l)}')
print(f'Результат умножения двух чисел: {mul_hex(num1_l, num2_l)}')
