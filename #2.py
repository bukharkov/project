n = int(input('Введите количество элементов в списке:'))
m = 0
my_list = []
my_list1 = []
i = 1
while m < n:
    el = input('Введите элемент списка: ')
    my_list.append(el)
    m += 1
print(f'Изначальный список {(my_list)}')
if n % 2 == 0:
    while i < n:
        my_list1.append(my_list[i])
        my_list1.append(my_list[i - 1])
        i += 2
    print(f'Измененный список {(my_list1)}')
else:
    while i < (n - 1):
        my_list1.append(my_list[i])
        my_list1.append(my_list[i - 1])
        i += 2
    my_list1.append(my_list[i-1])
    print(f'Измененный список {(my_list1)}')



