
class Date:

    def __init__(self, date):
        self.date = date

    def get_data(self):
        try:
            day, month, year = self.date.split(".")
            return int(day), int(month), int(year)
        except Exception:
            print(f"Не удалось выделить дату!")

    @staticmethod
    def validate_data(date_input):
        try:
            day, month, year = date_input
            if day not in range(1, 32):
                raise ValueError('День указан некорректно!')
            elif month not in range(1, 13):
                raise ValueError('Месяц указан некорректно!')
            elif year not in range(0, 2100):
                raise ValueError('Год указан некорректно!')
        except ValueError as err:
            print(err)
        else:
            print("Дата провалидирована!")




my_date_init = Date('05.10.2015')
my_date = my_date_init.get_data()
print(my_date)
if my_date:
    my_date_cls.validate_data(my_date)