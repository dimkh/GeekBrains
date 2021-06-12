# Проверку введённых значений на корректность не провожу
# (примеры проверок в начальных заданиях)

print('Работаем с латинским алфавитом...')
s1 = input('Введите первую букву: ').upper()
s2 = input('Введите вторую букву: ').upper()

first_letter = ord('A')
place_s1 = ord(s1) - first_letter + 1
place_s2 = ord(s2) - first_letter + 1
between_ss = place_s2 - place_s1 - 1

print(f"Буква {s1} находится на {place_s1}-м месте алфавита.")
print(f"Буква {s2} находится на {place_s2}-м месте алфавита.")
print(f"Между ними {between_ss} букв.")