# задание №2
def my_func(first_name, last_name, year, city, eml, phone):
    return (f'Имя: {first_name}   Фамилия: {last_name}   Возраст: {year}   Город: {city}   Email: {eml}   Телефон: {phone}')
first_name = input('Имя: ')
last_name = input('Фамилия: ')
year = input('возраст: ')
city = input('город: ')
eml = input('email: ')
phone = input('телефон: ')
print(my_func(first_name, last_name, year, city, eml, phone))