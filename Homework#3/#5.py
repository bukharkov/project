#5

def sum_of_string(init_string):
    init_list = init_string.split()
    my_sum = 0
    for el in init_list:
        if el:
            try:
                if el == 'Y':
                    return my_sum, False
                else:
                    my_sum += int(el)
            except ValueError:
                continue
    return my_sum,True
c_flag = True
final_sum = 0
while c_flag:
    init_string = input('Введите числа через пробел, для завершения введите Y: ')
    current_sum, c_flag = sum_of_string(init_string)
    final_sum += current_sum
    print(f'Промежуточная сумма: {final_sum}')
print(f'Общая сумма: {final_sum}')



