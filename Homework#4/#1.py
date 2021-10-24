#1

from sys import argv

script_name, productivity, hour_rate, bonus = argv
print('Script name: ', script_name)
print('Productivity, h: ', productivity)
print('Rate per hour, rub/h: ', hour_rate)
print('Bonus, rub:', bonus)
print('Salary, rub:', salary)
print('Salary, rub: ', int(productivity) * int(hour_rate) + int(bonus))