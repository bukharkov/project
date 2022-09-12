
""" Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19 """

my_list = [1.1, 1.2, 3.1, 5, 10.01]
resid_list = []

for el in my_list:
    if (el*10)%10 != 0:
        resid_list.append((el * 10) % 10)

a = round((max(resid_list) - min(resid_list))/10, 2)

print(resid_list)
print(a)
print(type(a))




