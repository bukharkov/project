""" Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
 Известно, что при хранении данных используется принцип: одна строка — один пользователь.
 Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
  *Сохранить словарь в файл users_hobby.txt. Фрагмент файла с данными о пользователях (users.txt): Иванов Иван Иванович Петров Петр Петрович
  Фрагмент файла с данными о хобби (hobby.txt): скалолазание, охота горные лыжи"""

with open('users.txt', 'w+') as u:
    u.write('Иванов Иван Иванович\nПетров Петр Петрович')


with open('hobby.txt', 'w+') as h:
    h.write('скалолазание, охота\nгорные лыжи')

keys = []
values = []

with open('users.txt', 'r') as u:
    for line in u:
      keys.append(line)

with open('hobby.txt', 'r') as h:
    for line in h:
      values.append(line)


my_dict = dict(zip(keys, values))


with open('users_hobby.txt', 'w') as u_h:
    for key, val in my_dict.items():
        u_h.write(f'{key}:{val}')

