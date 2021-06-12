a = 5
b = 6

a_and_b = (a & b)
a_or_b = (a | b)
a_shift_left = (a << 2)
a_shift_right = (a >> 2)

print(f"Побитовое И над числами 5 и 6: {a_and_b}")
print(f"Побитовое ИЛИ над числами 5 и 6: {a_or_b}")
print(f"Побитовый сдвиг влево на 2 знака числа 5 (умножение на 2*2): {a_shift_left}")
print(f"Побитовый сдвиг вправо на 2 знака числа 5 (деление на 2*2): {a_shift_right}")