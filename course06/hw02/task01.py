def is_right_sign(sign_op: str) -> bool:
    """ Проверка разрешенной операции.
    На входе: операция
    На выходе: true, если операция разрешена и false в случае ошибки
    """
    operations = tuple('0+-*/')
    result = False
    if sign_op in operations:
        result = True
    return result


a, b = 1, 1
sign = '#'
while True:
    a, b = list(map(int, input('Введите два числа (через пробел)').split()))
    while True:
        sign = input('Введите знак операции (0 - выход)')
        if is_right_sign(sign):
            break
        else:
            print('Неразрешённая операция!')

    if sign == '0':
        break
    elif sign == '+':
        res = a + b
    elif sign == '-':
        res = a - b
    elif sign == '*':
        res = a * b
    else:
        res = a / b
    print(f"{a}{sign}{b}={res}")
