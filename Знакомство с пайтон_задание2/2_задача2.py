""" Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

Пример:

- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4) """

N = int(input('Введите чило: '))
a = list(range(1, N+1))
my_list = []
p = 1

for i in a:
    p *=i
    my_list.append(p)

print(my_list)




