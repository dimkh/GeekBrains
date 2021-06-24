str_limit = 10
el_start = 32
el_finish = 127
el_current = el_start
i = 1

print("Вывод элементов и их кодов в формате код-символ:")
while el_current < el_finish + 1:
    print(f"{el_current}-{chr(el_current)};", end=' ')
    if i % str_limit == 0:
        print('')
    i += 1
    el_current += 1
