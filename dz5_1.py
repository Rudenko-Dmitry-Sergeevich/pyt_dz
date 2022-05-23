# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.
my_file = open('new_file.txt', 'w')
while True:
    i = input('введите строку: ')
    my_file.write(i + '\n')
    if not i:
        break
my_file.close()
with open('new_file.txt') as new_file:
    for line in new_file:
        print(line)