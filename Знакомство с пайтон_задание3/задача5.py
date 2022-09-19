
"""Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]"""


n = input("Номер элемента ряда Фибоначчи: ")
n = int(n) - 2
fib1 = fib2 = 1
my_list = [0, fib1, fib2]
f1 = 1
f2 = -1
neg_list = [f1, f2]
while n > 0:
    fib1, fib2 = fib2, fib1 + fib2
    f1, f2 = f2, f1 - f2
    my_list.append(fib2)
    neg_list.append(f2)
    n -= 1
neg_list.reverse()
result = neg_list + my_list

print(result)





