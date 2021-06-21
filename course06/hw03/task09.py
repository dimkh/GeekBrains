import random as rnd

# Размеры матрицы
count_row = 5
count_col = 5

def print_matrix(mtrx: list) -> None:
    """ Красивый вывод матрицы из целых чисел.
    На входе: матрица.
    """

    # Разный вывод для двумерной и одномерной матриц
    if isinstance(mtrx[0], list):
        for i in range(len(mtrx)):
            for j in range(len(mtrx[0])):
                print(f'{mtrx[i][j]:4}', end = ' ')
            print()
    else:
        for i in range(len(mtrx)):
            print(f'{mtrx[i]:4}', end = ' ')
        print()

# Генерируем исходную матрицу
max_elem = 10
matrix = list()
for i in range(count_row):
    row = [rnd.randint(1, max_elem) for _ in range(count_col)]
    matrix.append(row)

print('Исходная матрица:')
print_matrix(matrix)

# Находим min элемент в столбцах
row_min = [9999] * count_col

for i in range(count_row):
    for j in range(count_col):
        if matrix[i][j] < row_min[j]:
            row_min[j] = matrix[i][j]

print('Минимальные элементы в столбцах:')
print_matrix(row_min)

print(f'\nМаксимальный элемент среди минимальных: {max(row_min)}\n')