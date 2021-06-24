import cProfile

# Алгоритм поиска простых чисел (решето Эратосфена)
def main():
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

    print(f'Количество простых чисел в диапазоне от 1 до {n}:')
    #print(primes)
    print(len(primes))


cProfile.run('main()')
#main()
