# Задание 1. Машина.
# Напишите программу в ООП стиле для контролирования движения машины.
# Что надо сделать:
# - создать класс “Car” (Машина).
# - Свойства, которые должны задаваться при создании экземпляра класса:
# - Цвет
# - Количество топлива
# - Расход топлива на 100 км
# - Пробег - по умолчанию 0
# - Методы, которые должны быть у машины:
# - drive
# - Принимает в себя аргумент - количество км, которые надо
# проехать. Если топлива хватает - уменьшаем количество
# топлива, пишем “Мы проехали … км”. Если не хватает - пишем
# “Не хватает топлива”
# - get_mileage
# - Возвращает пробег

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
            print(f'Мы проехали {km_number} км')
            print(f'Осталось топлива {self.fuel_quantity} л')
            self.mileage += km_number
        else:
            print('Не хватает топлива')

    def get_mileage(self):
        mileage_str = f'Пробег: {self.mileage} км'
        return mileage_str


car = Car('красная', 50, 10, 70)
car.drive(20)
car.drive(480)
print(car.get_mileage())