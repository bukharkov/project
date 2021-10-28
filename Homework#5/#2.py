with open('Text1') as textfile:
    list_of_lines = textfile.readlines()
    print('Количество строк: ', len(list_of_lines))
    for number_of_line, line in enumerate(list_of_lines, 1):
        print(f'Количество слов в строке {number_of_line}: ', len(line.split()))