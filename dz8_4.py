# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру (например, словарь).
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

class Err(Exception):
    def __init__(self, txt):
        self.txt = txt

class Sklad:
    sklad = {'принтер': [], 'сканер': [], 'ксерокс': []}

    def sklad_add(self, a):
        try:
            if not isinstance(a[4], int):
                raise Err(f'ошибка ввода кол-во товара: {a[2]} - значение {a[4]}') # проверку сделал только на кол-во товара. При ошибке записывает значение "0" и выводит сообщение об ошибке
        except Err as err:
            a[4] = 0
            print(err)

        self.sklad[a[0]].append(a[1:])

    def sklad_info(self):
        print(self.sklad)
        [print(f'{i}: {sum([y[3] for y in self.sklad[i]])} шт.') for i in self.sklad.keys()] # подсчёт кол-во каждого класса оргтехники
        print(f'всего: {sum([y[3] for i in self.sklad.keys() for y in self.sklad[i]])} шт.') # подсчёт всего

class Office_equipment:
    def __init__(self, name, art, price):
        self.name = name
        self.art = art
        self.prie = price

class Printers(Office_equipment):
    def __init__(self, typ, typ_printer, name, art, quantity, price):
        self.quantity = quantity
        self.typ = typ
        self.typ_printer = typ_printer
        super().__init__(name, art, price)
    def printers(self):
        return [self.typ, self.typ_printer, self.name, self.art, self.quantity, self.prie]

class Scanners(Office_equipment):
    def __init__(self, typ, typ_scanner, name, art, quantity, price):
        self.quantity = quantity
        self.typ = typ
        self.typ_scanner = typ_scanner
        super().__init__(name, art, price)
    def scanners(self):
        return [self.typ, self.typ_scanner, self.name, self.art, self.quantity, self.prie]

class Copiers(Office_equipment):
    def __init__(self, typ, typ_copiers, name, art, quantity, price):
        self.quantity = quantity
        self.typ = typ
        self.typ_copiers = typ_copiers
        super().__init__(name, art, price)
    def copiers(self):
        return [self.typ, self.typ_copiers, self.name, self.art, self.quantity, self.prie]

printer1 = Printers('принтер', 'струйный', 'Epson L805', '123974', 4, 13193)
printer2 = Printers('принтер', 'лазерный', 'HP Laser 107', '952583', 5, 10256)
scanner1 = Scanners('сканер', 'цветной', 'HP ScanJet Pro 4500', '109593', 3, 9699)
scanner2 = Scanners('сканер', 'монохромный', 'Canon image Formula', '730985', 7, 12000)
scanner3 = Scanners('сканер', 'монохромный', 'Canon Formula', '730984', 1, 4000)
copier1 = Copiers('ксерокс', 'цветной', 'Xerox C230', '740174', 4,  8999)
copier2 = Copiers('ксерокс', 'монохромный', 'Xerox Phaser 8200', '301845', 8, 7999)

sklad = Sklad()

sklad.sklad_add(printer1.printers())
sklad.sklad_add(printer2.printers())

sklad.sklad_add(scanner1.scanners())
sklad.sklad_add(scanner2.scanners())
sklad.sklad_add(scanner3.scanners())

sklad.sklad_add(copier1.copiers())
sklad.sklad_add(copier2.copiers())

sklad.sklad_info()