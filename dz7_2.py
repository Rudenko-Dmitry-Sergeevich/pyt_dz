# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

class Clothes:
    def __init__(self, v, h):
        self.v = v
        self.h = h
    @property
    def coat(self):
        self.fabric_consumption_coat = round(self.v / 6.5 + 0.5, 2)
        return f'расход ткани на пальто, если размер {self.v}: {self.fabric_consumption_coat}'
    @property
    def suit(self):
        self.fabric_consumption_suit = round(2 * self.h + 0.3, 2)
        return f'расход ткани на костюм, если рост {self.h}: {self.fabric_consumption_suit}'
    @property
    def total_abric_consumption(self):
        return f'общий расход ткани: {self.fabric_consumption_suit + self.fabric_consumption_coat}'

a = Clothes(48, 1.8)
print(a.coat)
print(a.suit)
print(a.total_abric_consumption)