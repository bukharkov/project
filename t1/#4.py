#4
number = int(input('Введите число: '))
max_n = 0
while number % 10 > 0:
    n = number % 10
    if n > max_n:
        max_n = n
    number = number // 10
print('Максимальная цифра в числе: ', max_n)