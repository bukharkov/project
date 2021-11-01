#4

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name}  цвета {self.color} едет со скоростью {self.speed}')

    def stop(self):
        print(f'Машина {self.name}  цвета {self.color} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name}  цвета {self.color} повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость машины {self.speed}')

class TownCar(Car):

    def show_speed(self):
        if self.speed() > 60:
            print("Вы превысили скорость!")
        else:
            Car.show_speed(self)

class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=False)

class WorkCar(Car):

    def show_speed(self):
        if self.speed() > 40:
            print("Вы превысили скорость!")
        else:
            Car.show_speed()



class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)

police_car = PoliceCar(100, "black", 'Ford')
police_car.go()
police_car.turn('Налево')
police_car.stop()
police_car.show_speed()


