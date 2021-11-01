#2

class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight_of_coverage(self, density, thickness):
        weight = self._length * self._width * density * thickness
        return weight

my_road = Road(10000, 25)
print(my_road.weight_of_coverage(30,1))