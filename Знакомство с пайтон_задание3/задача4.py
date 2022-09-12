
""" Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10 """

num = int(input('Введите число: '))
my_list = []

while num != 0:
    r = num % 2
    my_list.append(r)
    num = num//2

my_list.reverse()
my_list = (map(str,my_list))

print("".join(my_list))





