import hashlib

def get_substr_hash(st: str) -> list:
    """ Функция определяет все возможные подстроки в заданной строке.
    На входе: строка.
    На выходе: массив с подстроками
    """

    len_str = len(st)

    hash_lst = list()

    for i in range(len(st) + 1):
        for j in range(i + 1, len(st) + 1):
            hash = hashlib.sha1(st[i:j].encode('utf-8')).hexdigest()
            hash_lst.append(hash)

    return hash_lst


my_str = 'abc'
h_l = get_substr_hash(my_str)

print(f'\nЗаданная строка: {my_str}')
print(f'\nКоличество возможных подстрок: {len(h_l)}')

# Если хэши подстрок не нужны, можно из функции сразу же вернуть длину итогового списка -
# количество подстрок в заданной строке.
