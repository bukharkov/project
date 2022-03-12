initial_string = input('Введите строку из слов разделенных пробелами: ')
word_list = initial_string.split()
for i, word in enumerate(word_list, 1):
    print(i, word[:10])