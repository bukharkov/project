

"""
*Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
(значения от 0 до 100) многочлена и записать в файл многочлен степени k. 
Пример: k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
"""

from random import randint
import itertools

k = int(input('Введите степень: '))

ratios = [randint(0, 100) for el in range(k+1)]

def polynomial(k, ratios):
    var = ['*x^']*(k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x',' x')

polynom = polynomial(k, ratios)
print(polynom)

with open('polynom.txt', 'w') as p:
    p.write(polynom)







