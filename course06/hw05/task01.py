import collections

Plant = collections.namedtuple('Plant', ['name', 'kv1', 'kv2', 'kv3', 'kv4', 'year'])
plants = list()
count_plants = 4

# Для тестирования использую готовый набор данных.
# Если нужен ввод значений - делаю is_test = False.
is_test = True

if is_test:
    plants.append(Plant(name = 'ПАО Синтез', kv1 = 123.12, kv2 = 143.75, kv3 = 25.52, kv4 = 187.84, year = 480.23))
    plants.append(Plant(name = 'ЗАО Глинки', kv1 = 47.24, kv2 = 54.53, kv3 = 151.48, kv4 = 37.41, year = 290.66))
    plants.append(Plant(name = 'ПАО Курганмашзавод', kv1 = 174.45, kv2 = 80.12, kv3 = 76.39, kv4 = 142.59, year = 473.55))
    plants.append(Plant(name = 'ООО Омега', kv1 = 7.16, kv2 = 12.52, kv3 = 25.61, kv4 = 48.91, year = 94.2))
else:
    count_plants = int(input('Введите количество предприятий для анализа: '))
    for i in range(count_plants):
        print(f'\nВведите информацию по {i + 1}-му предприятию.')
        name = input('Название предприятия: ')
        kv1 = float(input('Прибыль за 1-й квартал: '))
        kv2 = float(input('Прибыль за 2-й квартал: '))
        kv3 = float(input('Прибыль за 3-й квартал: '))
        kv4 = float(input('Прибыль за 4-й квартал: '))
        year = kv1 + kv2 + kv3 + kv4
        plants.append(Plant(name = name, kv1 = kv1, kv2 = kv2, kv3 = kv3, kv4 = kv4, year = year))

# Расчет среднегодовой прибыли по всем предприятиям
avg_profit = 0
for i in range(count_plants):
    avg_profit += plants[i].year
avg_profit /= count_plants

print(f'\nПредприятия с прибылью выше среднего ({avg_profit}):')
for i in range(count_plants):
    if plants[i].year > avg_profit:
        print(f'{plants[i].name}, прибыль {plants[i].year}')

print(f'\nПредприятия с прибылью ниже среднего ({avg_profit}):')
for i in range(count_plants):
    if plants[i].year < avg_profit:
        print(f'{plants[i].name}, прибыль {plants[i].year}')
