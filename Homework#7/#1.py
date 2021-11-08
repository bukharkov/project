
class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        my_str = '\n'
        for list in self.matrix:
            for el in list:
                my_str += f'{el: > 5}'
            my_str += '\n'
        return my_str
    def __add__(self, other):
        add = []
        if len(self.matrix) != len(other.matrix):
            print('Проверьте размер!')
            return None
        for i in range(len(self.matrix)):
            if len(self.matrix[i]) != len(other.matrix[i]):
                print('Проверьте размер')
                return None
            list = []
            for j in range(len(self.matrix[i])):
                list.append(self.matrix[i][j] + other.matrix[i][j])
            add.append(list)

        return Matrix(add)

m1 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(f'm1 = {m1}')
m2 = Matrix([[11, 12, 13, 14], [15, 16, 17, 18], [19, 20, 21, 22]])
print(f'm2 = {m2}')
print(f"sum_of_matrixes = {m1 + m2}")

