#1

int_string = input('Введите строку: ')
with open('Text1', 'a') as textfile:
    while int_string:
        textfile.write(int_string+ '\n')
        int_string = input('Введите следующую строку: ')
