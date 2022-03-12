#4

init_list = [1, 1, 23, 41, 41, 41, 7, 9, 10, 10, 99, 87, 23, 5, 43, 94]

mod_list = [ el  for el in init_list if init_list.count(el) == 1 ]

print(mod_list)