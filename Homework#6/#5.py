#5

class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationary):

    def draw(self):
        super().draw()
        print(f'Мы рисуем {self.title}')


class Pencil(Stationary):

    def draw(self):
        super().draw()
        print(f'Мы рисуем {self.title}')


class Handle(Stationary):

    def draw(self):
        super().draw()
        print(f'Мы рисуем {self.title}')

pen = Pen('ручкой')
pencil = Pencil('карандашом')
handle = Handle('маркером')
pen.draw()
pencil.draw()
handle.draw()