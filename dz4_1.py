# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv
script_name, output_in_hours, rate_per_hour, prize = argv
print(f'название скрипта: {script_name}')
print(f'выработка в часах: {output_in_hours}')
print(f'ставка в час: {rate_per_hour}')
print(f'премия: {prize}')
print(f'заработная плата сотрудника: {int(output_in_hours) * int(rate_per_hour) + int(prize)}')



