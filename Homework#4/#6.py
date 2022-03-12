#6

from itertools import count, cycle

for el in count(3):
    if el > 10:
        break
    else:
        print(el)


nscionalidad = ['ruso', 'aleman', 'frances', 'chino', 'japones']
i = 0
for el in cycle(nscionalidad):
    if i > 15:
        break
    print(el)
    i +=1
