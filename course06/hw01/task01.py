st = '1'
while not st.isdigit() or len(st) != 3:
    st = input('Введите трехзначное число: ')

st_sum = int(st[0]) + int(st[1]) + int(st[2])
st_mul = int(st[0]) * int(st[1]) * int(st[2])

print(f"Сумма цифр равна {st_sum}")
print(f"Произведение цифр равно {st_mul}")