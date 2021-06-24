count_even, count_odd = 0, 0

num = int(input('Введите натуральное число:'))
num_orig = num
while num > 0:
    if num % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
    num //= 10

print(f"В числе {num_orig} {count_even} чётных цифр и {count_odd} нечётных.")
