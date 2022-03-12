#4

def pow_neg(x, y):
    x_power_y = 1
    if x <= 0:
        return
    elif y == 0:
        return 1
    elif y > 0:
        return
    else:
        while y < 0:
            x_power_y *= 1/x
            y += 1
        return x_power_y
x = int(input('x: '))
y = int(input('y: '))
result = pow_neg(x, y)
print(result if result else "Неверные данные!")

