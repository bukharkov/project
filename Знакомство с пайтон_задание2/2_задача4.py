"""Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число."""

N = int(input('Введите число: '))
a = list(range(-N, N+1))
my_list = []
p = 1
for i in a:
    p *=i
    my_list.append(p)

with open("file.txt", "w") as file:
    for i in my_list:
        file.write(str(i) + '\n')




