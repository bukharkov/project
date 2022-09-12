
""" Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15] """

my_list = [2, 4, 1, 3, 5, 3, 7, 8, 9, 3, 8]

my_list1 = list.copy(my_list)

mult_list = []

if (len(my_list)) % 2  != 0:
    for i in range(len(my_list)//2 + 1):
        mult_list.append(my_list[i] * my_list1[i])
else:
    for i in range(len(my_list)//2):
        mult_list.append(my_list[i] * my_list1[i])

print(my_list1)
print(my_list)
print(len(my_list))
print(mult_list)


