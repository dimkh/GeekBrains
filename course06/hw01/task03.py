# Проверка на число.
# Отрицательные и дробные числа тоже нужны.
def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

x1, y1, x2, y2 = '','','',''
sign = '+'

while not is_number(x1):
    x1 = input("Введите координату X1: ")
while not is_number(y1):
    y1 = input("Введите координату Y1: ")
while not is_number(x2):
    x2 = input("Введите координату X2: ")
while not is_number(y2):
    y2 = input("Введите координату Y2: ")
x1 = int(x1)
y1 = int(y1)
x2 = int(x2)
y2 = int(y2)

# Расчёт коэффициентов уравнения прямой
x3 = x2 - x1
y3 = y2 - y1
b = (y1 / y3 - x1 / x3) * y3
k = y3 / x3
if b < 0:
    sign = '-'
    b = b * (-1)

print(f"Уравнение прямой, проходящей через точки ({x1},{y1}) и ({x2},{y2}):")
print(f"y = {k} * x {sign} {b}")
