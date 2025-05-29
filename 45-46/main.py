# Продолжите работать над программой из прошлой домашки. Добавьте
# новый класс SportCar(), который наследуется от базового класса Car( )
# Внутри класса SportCar() добавьте метод fast_drive(), который будет
# работать также как drive(), только потребление топлива сделайте в
# полтора раза больше.
# Дополните класс методом competition() суть которого в том, чтобы с
# вероятностью 50% возвращать выиграла машина в соревнованиях или
# нет.

class Car:
    def __init__(self, color, fuel_quantity, fuel_consumption, mileage=0):
        self.color = color
        self.fuel_quantity = fuel_quantity  # количество
        self.fuel_consumption = fuel_consumption # расход
        self.mileage = mileage

    def drive(self, km_number):
        need_fuel = (self.fuel_consumption * km_number) / 100
        if need_fuel <= self.fuel_quantity:
            self.fuel_quantity -= need_fuel
            print(f'мы проехали {km_number} км')
            self.mileage += km_number
            self._add_textfile(km_number, self.fuel_quantity)
        else:
            print('не хватает топлива')

    def get_mileage(self):
        mileage_str = f'пробег: {self.mileage} км'
        return mileage_str

    def _add_textfile(self, km, fuel):
        with open('car info.txt', 'a', encoding='utf-8') as f:
            f.write(f'пройдено километров - {km}, топлива осталось - {fuel} л\n')

    def painting(self, new_color):
        car_colors = ["красный", "синий", "зеленый", "черный", "белый", "серый"]
        if new_color in car_colors:
            self.color = new_color
            print(f'машина перекрашена в {new_color}')
        else:
            print('цвета нет в списке допустимых')


class SportCar(Car):
    def fast_drive(self, km_number):
        need_fuel = (self.fuel_consumption * km_number * 1.5) / 100
        if need_fuel <= self.fuel_quantity:
            self.fuel_quantity -= need_fuel
            print(f'мы проехали {km_number} км')
            self.mileage += km_number
            self._add_textfile(km_number, self.fuel_quantity)
        else:
            print('не хватает топлива')

    def competition(self):
        import random
        rand = random.choice(['выиграл', 'проиграл'])
        return rand


car1 = Car('черный', 8, 8, 0)
car2 = SportCar('черный', 8,8, 0)

print('Первая машина')
for i in range(4):
    car1.drive(30)

print('\nВторая машина')
for i in range(4):
    car2.fast_drive(30)

print(car2.competition())
