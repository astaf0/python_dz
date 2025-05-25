# Задание 1
# Продолжите работать над программой из прошлой домашки.
# 1. Добавьте возможность логировать операции с машиной. То есть
# необходимо записывать в файл расстояние и количество топлива
# для каждого вызова метода drive()
# Сделайте это либо с добавлением приватного метода либо с
# помощью второго класса.
# 2. Добавьте метод для покраски машины. Он должен принимать в
# себя цвет. Если цвет есть в списке допустимых, то цвет должен
# измениться. Если нет - выводите сообщение. Список допустимых
# цветов определите сами.

class Car:
    def __init__(self, color, fuel_quantity, fuel_consumption, mileage=0):
        self.color = color
        self.fuel_quantity = fuel_quantity  # количество
        self.fuel_consumption = fuel_consumption # расход
        self.mileage = mileage

    def drive(self, km_number):
        need_fuel = km_number / self.fuel_consumption

        if need_fuel <= self.fuel_quantity:
            self.fuel_quantity -= need_fuel
            print(f'мы проехали {km_number} км')
            print(f'осталось топлива {self.fuel_quantity} л\n')
            self.mileage += km_number
            self._add_textfile(km_number, self.fuel_quantity)
        else:
            print('не хватает топлива\n')

    def get_mileage(self):
        mileage_str = f'пробег: {self.mileage} км'
        return mileage_str

    def _add_textfile(self, km, fuel):
        with open('car info.txt', 'a', encoding='utf-8') as f:
            f.write(f'пройдено километров - {km}, топлива осталось - {fuel} л\n')

    def painting(self, new_color):
        car_colors = [
            "красный", "синий", "зеленый",
            "черный", "белый", "серый"
        ]
        if new_color in car_colors:
            self.color = new_color
            print(f'машина перекрашена в {new_color}')
        else:
            print('цвета нет в списке допустимых')



car = Car('красный', 50, 10, 70)
car.drive(20)
car.drive(480)
car.drive(30)

print(car.get_mileage())

car.painting('черный')
car.painting('фиолетовый')