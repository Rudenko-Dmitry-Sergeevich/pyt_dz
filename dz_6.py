# задание №6
x = 1
m = []
m1 = {}
name1 = []
price1 = []
quantity1 = []
ed1 = []
while True:
    name = input('название: ')
    price = input('цена: ')
    quantity = input('количество: ')
    ed = input('единица измерения: ')
    n = (x, {'название': name, 'цена': price, 'количество': quantity, 'ед.': ed})
    m.append(n)
    x += 1
    s = input('(Ввести еще позицию? ДА ==> любая клавише; НЕТ ==> n)')
    if s == 'n':
        break
print(f'структура характеристик: {m}')
for i in range(len(m)):
    name1.append(m[i][1]['название'])
    price1.append(m[i][1]['цена'])
    quantity1.append(m[i][1]['количество'])
    ed1.append(m[i][1]['ед.'])
m1['названия'] = name1
m1['цены'] = price1
m1['количество'] = quantity1
m1['ед.'] = set(ed1)
print(f' собранная аналитика: {m1}')