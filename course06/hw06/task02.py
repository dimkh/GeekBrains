n = 9592            # Найти 9592 первых простых чисел (100000 для решета Эратосфена)
primes = []         # Список простых чисел

# После первых 3 простых чисел (2, 3, 5) можно проверять только числа, оканчивающиеся
# на 1, 3, 7 или 9, т.к. остальные точно делятся на 2 или 5.
i = 2
while len(primes) < n:
    # Проверяем текущее число на делимость уже найденными простыми числами
    for j in range(len(primes)):
        if i % primes[j] == 0:
            break
    else:
        primes.append(i)
    i += 1

var_size = i.__sizeof__()
var_size += n.__sizeof__()
var_size += primes.__sizeof__()

print(f'\nПеременная i: {i.__sizeof__()} байт')
print(f'Переменная n: {n.__sizeof__()} байт')
print(f'Переменная primes: {primes.__sizeof__()} байт')
print(f'Общий объём занимаемой памяти: {var_size} байт\n')
