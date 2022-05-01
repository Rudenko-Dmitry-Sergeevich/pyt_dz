# задание №1
def n(a, b):
    return a / b
a = int(input('введите число a: '))
b = int(input('введите число b: '))
if b != 0:
    print(n(a, b))
else:
    print('неверные данные!')