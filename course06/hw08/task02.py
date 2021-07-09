import heapq
from collections import Counter

# В объектах класса Leaf хранятся уникальные символы из заданной строки
class Leaf:

    symbol: str

    def __init__(self, smbl: str) -> None:
        self.symbol = smbl

    def get_code(self, code: dict, prefix: str):
        code[self.symbol] = prefix or '1'   # Если строка из одного символа - префикса нет, кодируем единичкой


# В объектах класса Node хранятся узлы дерева, содержат ссылки на левого и правого потомков
class Node:

    left_el: None
    right_el: None

    def __init__(self, left, right) -> None:
        self.left_el = left
        self.right_el = right

    def get_code(self, code: dict, prefix: str):
        self.left_el.get_code(code, f'{prefix}1')
        self.right_el.get_code(code, f'{prefix}0')


def huffman(str4code: str) -> dict:
    """ Функция формирует кодовую таблицу с использованием алгоритма Хаффмана.
    На входе: строка.
    На выходе: словарь с таблицей символов и их кодами.
    """

    # Заполняем очередь с приоритетом символами заданной строки и их количеством (весами)
    heap = []
    for symbol, weight in Counter(str4code).items():
        heap.append((weight, len(heap), Leaf(symbol)))  # Длина очереди - для сортировки кучи при равенстве весов
    heapq.heapify(heap)

    count = len(heap)

    while len(heap) > 1:        # Обрабатываем очередь, пока есть хотя бы 2 элемента
        # Извлекаем из очереди 2 элемента с минимальными весами
        freq1, _, left_el = heapq.heappop(heap)
        freq2, _, right_el = heapq.heappop(heap)
        # Добавляем новый узел с суммой этих весов и ссылками на извлечённых потомков
        heapq.heappush(heap, (freq1 + freq2, count, Node(left_el, right_el)))
        count += 1

    # В очереди остался один элемент - корневой
    # Формируем таблицу кодов символов
    code = {}
    heap[0][2].get_code(code, '')

    return code

# Для проверки - уже разобранную на занятиях строку
my_str = 'beep boop beer!'

#my_str = 'aaaaa   333'

# Заполнение словаря - таблицы кодов
if len(my_str) > 0:
    ds = huffman(my_str)
    print(f'\nТаблица кодов:')
    print(ds)

# Кодировка заданной строки
result = ''
for symbol in my_str:
    #result = f'{result},{ds[symbol]}'       # Для проверки - оставлена запятая между символами
    result = f'{result}{ds[symbol]}'

print(f'\nЗадана строка: {my_str}')
print(f'\nОна же после кодировки Хаффмана')
print(result, '\n')
