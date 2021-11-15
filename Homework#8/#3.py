
class MyException(Exception):
    def __init__(self):
        self.text = 'Некорректные данные! Введите число!'

list = []
init_string = input('Введите число. Для выхода введите пробел:')

while init_string != ' ':
    try:
        if init_string.isdigit():
            list.append(int(init_string))
        else:
            raise MyException
    except MyException as err:
        print(err.text)

    init_string = input('Введите число. Для выхода введите пробел:')

print(list)
