#2
total_seconds = int(input('Введите время в секундах: '))
hours = total_seconds // 3600
residual_seconds = total_seconds % 3600
minutes = residual_seconds // 60
seconds = residual_seconds % 60
print(f"Итого: {hours} час(ов), {minutes} минут, {seconds} секунд")