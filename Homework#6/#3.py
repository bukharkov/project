#3

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):

    def get_full_name(self):
        return f"Имя: {self.name} Фамилия: {self.surname}"

    def get_total_income(self):
        return int(self._income['wage']) + int(self._income['bonus'])

position = Position('Sergey', 'Sergeev', 'analyst', 100000, 40000)
full_name = position.get_full_name()
total_income = position.get_total_income()
print(f"Total income of {full_name} is {total_income} rub")
