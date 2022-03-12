#3

def sum_of_max(a, b, c):
    my_list = [a, b, c]
    my_list.sort()
    my_list.reverse()
    return sum(my_list[:2])
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
print(sum_of_max(a, b, c))