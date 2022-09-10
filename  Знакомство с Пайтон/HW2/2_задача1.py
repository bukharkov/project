
num = int(input('Введите число '))

mylist = ['qwer', 'asdf', '2456', '24', 'dpo', '7']

def find_number(n, lst):
    return str(n) in lst

print(find_number(num, mylist))



