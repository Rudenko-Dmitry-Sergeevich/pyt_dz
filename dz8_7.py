# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число». Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        print(f' ({self.a}+{self.b}j) + ({other.a}+{other.b}j) ', end='')
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        print(f' ({self.a}+{self.b}j) * ({other.a}+{other.b}j) ', end='')
        return ComplexNumber(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)


    def __str__(self):
        return f"= {self.a}+{self.b}j"

mc_1 = ComplexNumber(3, 4)
mc_2 = ComplexNumber(2, 3)
mc_3 = ComplexNumber(2, 3)
print(mc_1 * mc_2 * mc_3)
print(mc_1 + mc_2)












