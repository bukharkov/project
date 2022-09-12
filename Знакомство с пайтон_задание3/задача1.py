
"""Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12"""

my_list = [3, 7, 9, 3, 4, 5, 7, 2, 4, 9]

# for i in range(len(my_list)):
#     if i%2 != 0:
#         odd_list.append(my_list[i])
# print(sum(odd_list))

odd_list = [my_list[i] for i in range(len(my_list)) if i % 2 != 0]

print(sum(odd_list))




