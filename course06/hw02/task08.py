count_num = int(input('Введите количество чисел в последовательности: '))
find_num = input('Введите цифру, которую будем искать: ')

count_symbol = 0
for i in range(count_num):
    cur_num = input(f'Введите {i + 1}-е число: ')
    count_symbol += cur_num.count(find_num)

print(f'Цифра {find_num} встретилась в последовательности {count_symbol} раз.')
