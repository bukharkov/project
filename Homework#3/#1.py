#1

def func_div(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return 'Деление на ноль!'
a = int(input('Введите делимое: '))
b = int(input('Введите делитель: '))
print(func_div(a, b))


