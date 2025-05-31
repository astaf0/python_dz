from datetime import datetime

class Model:
    def add_purchase(self, name, cost):
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        purchase = f'{name} - {cost} - {date} - \n'
        with open('purchases.txt', 'a', encoding='utf') as f:
            f.write(purchase)

    def read_purchases(self):
        purchases_list = []
        with open('purchases.txt', 'r', encoding='utf-8') as f:
            for line in f:
                purchases_list.append(line.split(' - '))
        return purchases_list


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def choice_1(self, name, cost):
        self.model.add_purchase(name, cost)
        self.view.print_message()

    def choice_2(self):
        list = self.model.read_purchases()
        self.view.print_purchases(list, len(list))

    def choice_3(self):
        list = self.model.read_purchases()
        sorted_list = sorted(list, key=lambda list: int(list[1]), reverse=True)
        self.view.print_purchases(sorted_list, 5)


class View:
    def print_message(self):
        print('Покупка добавлена')

    def print_purchases(self, list, i):
        counter = 1
        for purchase in list:
            print(f'{counter}. {purchase[0]} - {purchase[1]} руб. - {purchase[2]}')
            counter += 1
            if counter > i:
                break

    def input_error(self):
        print('Неверный ввод')

    def exit(self):
        print('Выход из программы')


v = View()
m = Model()
c = Controller(m, v)


while True:
    print('\nМеню:')
    print('1. Добавить покупку')
    print('2. Показать все покупки')
    print('3. Показать 5 самых дорогих покупок')
    print('4. Выход')
    choice = input('Выберите пункт меню: ')
    if choice == '1':
        p_name = input('Введите название товара: ')
        p_cost = input('Введите стоимость: ')
        c.choice_1(p_name, p_cost)
    elif choice == '2':
        c.choice_2()
    elif choice == '3':
        c.choice_3()
    elif choice == '4':
        c.view.exit()
        break
    else:
        c.view.input_error()