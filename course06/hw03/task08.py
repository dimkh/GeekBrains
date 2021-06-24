import random as rnd

# Заданы размеры матрицы (без столбика с суммой строк)
count_row = 5
count_col = 5

# is_demo == True - матрица генерируется автоматически, False - ввод с клавиатуры
is_demo = True
max_elem = 10

matrix = list()
for i in range(count_row):
    if not is_demo:
        row = list(map(int, input(f'Введите {i+1}-ю строку матрицы {count_row}x{count_col} (через пробел): ').split()))
    else:
        row = [rnd.randint(1, max_elem) for _ in range(count_col)]
    row.append(sum(row))
    matrix.append(row)

print('Итоговая матрица:')
for i in range(count_row):
    for j in range(count_col+1):
        print(f'{matrix[i][j]:4}', end = ' ')
    print()
