#6
#part1
number_of_goods = int(input('Введите количество позиций: '))
i = 0
my_sample =[]
while i < number_of_goods:
    my_dict = ({'название': input('Введите название товара: '), 'цена': input('Введите цену товра: '),
               'количество': input('Введите количество: '), 'ед': input('Введите ед измерения: ')})
    my_sample.append(((i+1), my_dict))
    i+=1
print(my_sample)

#part2
result_dict = {}
for structure in my_sample:
    number, struct_dict = structure
    for key, value in struct_dict.items():
        value_list = result_dict.get(key, [])
        if value not in value_list:
            value_list.append(value)
        result_dict[key] = value_list
print(result_dict)
