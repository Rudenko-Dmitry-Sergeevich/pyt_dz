# задание №4
def my_func(x, y):
    a = 1
    for i in range(y * -1):
        a *= x
    b = 1 / a
    return b
x = int(input('положительное число x: '))
y = int(input('отрицательное число y: '))
print(my_func(x, y))