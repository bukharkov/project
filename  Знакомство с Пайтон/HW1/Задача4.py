"""Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)."""

n = int(input("Введите номер четверти (от 1 до 4): "))
if n == 1:
     print(f"Допустимые значения для {n} четверти: x > 0, y > 0")
elif n == 2:
   print(f"Допустимые значения для {n} четверти: x < 0, y > 0")
elif n == 3:
   print(f"Допустимые значения для {n} четверти: x < 0, y < 0")
elif n == 4:
   print(f"Допустимые значения для {n} четверти: x > 0, y < 0")
else:
   print("Некорректные данные!")