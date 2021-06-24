import random as rnd

count = 0
num = rnd.randint(0, 100)
print('Загадано целое число из диапазона от 0 до 100 (включительно).')
print('Отгадайте это число! У Вас 10 попыток...')

while count < 10:
    user_num = int(input('Введите число: '))
    if user_num == num:
        print('Поздравляем! Вы отгадали! Победа!!!')
        break
    elif user_num < num:
        print('Увы, больше...')
    else:
        print('Увы, меньше...')
    count += 1
else:
    print(f'Печалька... Вы проиграли! А загадано было число {num}.')
    print('Может быть, повезёт в другой раз...')
