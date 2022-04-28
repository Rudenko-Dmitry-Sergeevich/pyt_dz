# задание №2
n = input("Введите числа через пробел: ").split()
for i in range(0, len(n) - 1, 2):
    n[i], n[i + 1] = n[i + 1], n[i]
for i in n:
    print(i, end = ' ')


