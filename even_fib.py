fib = [1, 2]
# Список чисел Фибоначчи.
even_fib = [0, 2]
# Список чётных числе Фибоначчи.

def even_fib_coun(x):
    '''
    Расчёт чисел Фибоначчи и запись их в список.
    Запись в отдельный список чётных чисел.
    '''
    a = fib[0]
    b = fib[1]
    while len(even_fib) != x:
        c = a + b
        a = b
        b = c
        fib.append(c)
        # Запись числа Фибоначчи с список.
        remainder = c % 2
        if remainder == 0:
            # Если число чётное, запись его в список с чётными числами.
            even_fib.append((c))
        else:
            continue

even_fib_coun(4)

print(', '.join(map(str,even_fib)))
# Вывод чётных чисел Фибоначчи через запятую.
