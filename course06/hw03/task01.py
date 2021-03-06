# Итоговый список с результатами
res_lst = [0] * 8

# Пробегаем по всем натуральным числам диапазона
for i in range(2, 100):
    # Каждое число проверяем на кратность
    for j in range(2, 10):
        # Кратно - добавляем 1 в итоговый список
        if i % j == 0:
            res_lst[j - 2] += 1

# Вывод результатов
i = 2
print('В диапазоне от 2 до 99 кратных чисел:')
for elem in res_lst:
    print(i, ' - ', res_lst[i - 2])
    i += 1
