# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
class Data:
    def __init__(self, data):
        self.data = data
    @classmethod
    def data_int(cls, x):
        return [int(i) for i in x.data.split('-')]
    @staticmethod
    def number_validation(y):
        if not 1 < y[0] < 32:
            return f'недопустимое значение "день"'
        elif not 1 < y[1] < 12:
            return f'недопустимое значение "месяц"'
        elif not 1900 < y[2] < 3000:
            return f'недопустимое значение "год"'
        else:
            return f'валидация: ok'

d = Data('31-05-2022')

print(d.data)
print(f'{type(d.data)}\n')

print(Data.data_int(d))
print(f'{[type(i) for i in Data.data_int(d)]}\n')

print(Data.number_validation(Data.data_int(d)))
