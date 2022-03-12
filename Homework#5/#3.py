#3
total_salary = 0
with open('salary#3') as file:
    lines = file.readlines()
    for line in lines:
        surname, salary = line.split()
        total_salary += int(salary)
        if int(salary) < 20000:
            print(f'{surname} имеет оклад менее 20 тысяч руб.')
print('Средний оклад сотрудников:', total_salary/len(lines))
