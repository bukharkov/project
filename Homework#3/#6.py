#6

capitalize_func = lambda word: word.capitalize()

init_string = input('Введите строку: ')
final_string_list = []
input_words = init_string.split()
for el in input_words:
    final_string_list.append(capitalize_func(el))
print(' '.join(final_string_list))