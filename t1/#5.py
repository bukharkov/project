revenue = int(input('Введите значение выручки компании: '))
costs = int(input('Введите значение издержек: '))
if revenue < costs:
    print('Компания понесла убытки')
elif revenue == costs:
    print('Компания отработала в ноль')
else:
    print(f"Компания получила прибыль: {revenue - costs} руб." )
    print(f'Рентабельность выручки составляет: {(revenue - costs) / revenue}')
    n_workers = int(input('Введите количество раотников компании: '))
    print(f"Прибыль в расчете на одного сотрудника составляет: {(revenue - costs) / n_workers} руб.")
