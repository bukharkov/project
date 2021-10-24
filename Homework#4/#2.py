#2

init_list = [2, 7, 3, 10, 3, 3, 88, 77, 54, 97]

print('Initial list:', init_list)

def modified_list():

    mod_list = [ init_list[i] for i in range(1, len(init_list)) if init_list[i-1] < init_list[i]]

    return (mod_list)

print('Modified list: ', modified_list())