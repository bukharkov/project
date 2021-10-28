language_dict = {'One': 'Один',
                 'Two': 'Два',
                 'Three': 'Три',
                 'Four': 'Четыре'}
with open('text#4', 'r+') as file_r, open('text#4_1', 'w+') as file_w:
    for line in file_r.readlines():
        text_n, number = line.split(' - ')
        print(line.split(' - '))
        file_w.write(f'{language_dict[text_n]} - {number}\n')