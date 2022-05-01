# задание №5
b = 0
c = 0
while True:
    if c == 'n':
        break
    a = input('введите числа через пробел, чтобы остановить программу введите <n>')
    a = a.split()
    for i in range(0,len(a)):
        if a[i] == 'n':
            c = 'n'
            break
        b += int(a[i])
    print(f'сумма чисел: {b}')