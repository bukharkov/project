#6
first_result = int(input('Введите первоначальный результат спортсмена: '))
target_result = int(input('Введите целевой результат: '))
n = 1
while first_result < target_result:
    first_result = first_result * 1.10
    n += 1
print(f'Спортсмен достигнет целвой результат на {n} день')
