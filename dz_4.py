# задание №4
n = input("введите слова через пробел: ").split()
for x, y in enumerate(n, start = 1):
    print(f'№{x}:{y[:10]}')