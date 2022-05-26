# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return f'машина {self.name} поехала'
    def stop(self):
        return f'машина {self.name} остановилась'
    def turn(self, direction):
        return f'направление:{direction}'
    def show_speed(self):
        return f'скорость:{self.speed}'

class Town(Car):
    town_car = 'городской автомобиль'
    def show_speed(self):
        if self.speed > 60:
            return f'привышение скорости на {self.speed - 60}'
        else:
            return f'скорость:{self.speed}'

class Sport(Car):
    sport_car = 'спортивный автомобиль'

class Work(Car):
    work_car = 'рабочий автомобиль'
    def show_speed(self):
        if self.speed > 40:
            return f'привышение скорости на {self.speed - 40}'
        else:
            return f'скорость:{self.speed}'

class Police(Car):
    police_car = 'полицейский автомобиль'

town = Town(45, 'синий', 'lada', False)
print(f'{town.town_car} \nцвет:{town.color}  марка:{town.name}  полицейская:{town.is_police}')
print(f'{town.go()} ==> {town.show_speed()} | {town.turn("лево")} | {town.stop()}\n')

sport = Sport(145, 'зеленый', 'gaz-007', False)
print(f'{sport.sport_car} \nцвет:{sport.color}  марка:{sport.name}  полицейская:{sport.is_police}')
print(f'{sport.go()} ==> {sport.show_speed()} | {sport.turn("право")} | {sport.stop()}\n')

work = Work(45, 'черный', 'Lexus', False)
print(f'{work.work_car} \nцвет:{work.color}  марка:{work.name}  полицейская:{work.is_police}')
print(f'{work.go()} ==> {work.show_speed()} | {work.turn("лево")} | {work.stop()}\n')

police = Police(245, 'синий', 'Mazda', True)
print(f'{police.police_car} \nцвет:{police.color}  марка:{police.name}  полицейская:{police.is_police}')
print(f'{police.go()} ==> {police.show_speed()} | {police.turn("лево")} | {police.stop()}\n')


