"""
Напишите программу, которая принимает на вход цифру,
обозначающую день недели, и проверяет, является ли этот день выходным.

Пример:

- 6 -> да
- 7 -> да
- 1 -> нет
"""

x = int(input('Введите цифру обозначающую день недели (1-7): '))
if x in list(range(1,6)):
    print('Это будний день')
elif x in list(range(6,8)):
    print('Это выходной')
else:
    print('Некорректные данные')


