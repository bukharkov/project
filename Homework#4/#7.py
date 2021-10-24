#7
from itertools import count
def fact(n):
    f =1
    for i in count(1):
        if i <= n:
            f *= i
            yield f
        else:
            break
for el in fact(10):
    print(el)
