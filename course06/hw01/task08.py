# Проверку введённых значений на корректность не провожу
# (примеры проверок в начальных заданиях)

leap_year = False
year = int(input('Введите год: '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            leap_year = True
    else:
        leap_year = True

if leap_year:
    print(f"Год {year} високосный")
else:
    print(f"Год {year} невисокосный")