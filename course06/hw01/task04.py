import random as rnd

# Проверку введённых значений на корректность не провожу
# (примеры проверок в начальных заданиях)

print('Список генераторов:')
print('1 - Случайное целое число')
print('2 - Случайное вещественное число')
print('3 - Случайный символ')
choice = int(input('Выберите генератор: '))

start = input('Введине начальное значение диапазона: ')
finish = input('Введите конечное значение диапазона: ')

if choice == 1:
    result = rnd.randint(int(start), int(finish))
elif choice == 2:
    result = rnd.uniform(float(start), float(finish))
else:
    result = chr(rnd.randint(ord(start), ord(finish)))

print(f"Случайное значение из диапазона от {start} до {finish}: {result}")