initial_rating = [33, 24, 10, 8, 6, 4, 4, 2]
new_el = int(input('Введите новый элемент рейтинга: '))
i = 0
if new_el < (min(initial_rating)):
    initial_rating.append(new_el)
else:
    while i < len(initial_rating):
        if new_el > initial_rating[i]:
            initial_rating.insert(i, new_el)
            break
        i+=1
print(f'Новый рейтинг: {initial_rating}')