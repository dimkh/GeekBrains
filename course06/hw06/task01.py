n = 100000
# Создадим базовый список чисел из интервала [0, n]
nmbrs = [i for i in range(n + 1)]
nmbrs[1] = 0       # 1 - не простое число
primes = []        # Список простых чисел

i = 2
while i <= n:
    if nmbrs[i] != 0:
        primes.append(nmbrs[i])
        # Обнуляем текущее простое число и следующие кратные ему
        for j in range(i, n + 1, i):
            nmbrs[j] = 0
    i += 1

var_size = i.__sizeof__()
var_size += n.__sizeof__()
var_size += nmbrs.__sizeof__()
var_size += primes.__sizeof__()

print(f'\nПеременная i: {i.__sizeof__()} байт')
print(f'Переменная n: {n.__sizeof__()} байт')
print(f'Переменная nmbrs: {nmbrs.__sizeof__()} байт')
print(f'Переменная primes: {primes.__sizeof__()} байт')
print(f'Общий объём занимаемой памяти: {var_size} байт\n')
