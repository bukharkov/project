#1
from itertools import cycle
from time import sleep

class TrafficLight:
    colors = ('красный', 'желтый','зеленый')
    time = (7, 2, 4)
    message = ('red', 'yellow', 'green')

    def __init__(self, color):
        self.__color = color

    def running(self):
        tl_cycle = cycle(self.colors)
        for tl_color in tl_cycle:
            if self.__color == tl_color:
                print(self.message[self.colors.index(self.__color)])
                sleep(self.time[self.colors.index(self.__color)])
                self.__color = next(tl_cycle)

my_trafficlight = TrafficLight('желтый')
my_trafficlight.running()
