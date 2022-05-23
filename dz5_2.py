# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.
with open('new_file.txt', 'r', encoding='utf-8') as new_file:
    y = 1
    i = new_file.readlines()
    print(i)
    print(f'В файле {len(i)} строк')
    for x in i:
        print(f'{y}) str - {len(x.split())} слов')
        y +=1