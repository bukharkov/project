#5

with open('text#5', 'w') as file_w:
    int_numbers = input('Введите числа через пробел: ')
    print(int_numbers, file= file_w)

with open('text#5', 'r') as file_r:
    content_list = file_r.read().split()
    number_list = [int(number) for number in content_list]
    print(number_list)
    print(sum(number_list))

