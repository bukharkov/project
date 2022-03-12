
class Cell:
    def __init__(self, q):
        try:
            if q <= 0:
                raise ValueError('количество ячеек должно быть > 0')
            self.q = int(q)
        except TypeError:
            self.q = 1
            print('Проверьте корректность входных данных')
        except ValueError:
            print('Проверьте корректность входных данных')
            self.q = 1

    def __add__(self, other):
        return Cell(self.q + other.q)

    def __sub__(self, other):
        if self.q - other.q > 0:
            return Cell(self.q - other.q)
        else:
            print('Вычитание невозможно')

    def __mul__(self, other):
        return Cell(self.q * other.q)

    def __truediv__(self, other):
        return Cell(self.q // other.q)

    def make_order(self, param):
        return (('*' * param) + '\n') * (self.q // param) + '*' * (self.q % param)

cell_1 = Cell(9)
cell_2 = Cell(14)
print(cell_1.make_order(4))
print()
print(cell_2.make_order(5))

cell_3 = cell_2*cell_1
print(cell_3)
print(cell_3.make_order(20))

