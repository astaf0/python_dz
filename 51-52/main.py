from abc import ABC, abstractmethod
from rich.console import Console
from rich.table import Table
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

    def delete(self, index):
        with open('purchases.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            del lines[index]
        with open('purchases.txt', 'w', encoding='utf-8') as f:
            f.writelines(lines)


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

    def choice_5(self, index):
        list = self.model.read_purchases()
        if index in range(len(list)):
            self.model.delete(index)
            print('Покупка удалена')
        else:
            print('Покупки не существует')


class AbstractView(ABC):
    @abstractmethod
    def print_message(self):
        pass

    @abstractmethod
    def print_purchases(self, list, i):
        pass

    @abstractmethod
    def input_error(self):
        pass

    @abstractmethod
    def exit(self):
        pass


class RichView(AbstractView):
    def print_message(self):
        print('Покупка добавлена')

    def print_purchases(self, list, i):
        console = Console()
        table = Table(title="Покупки")
        table.add_column('N')
        table.add_column('название')
        table.add_column('цена')

        counter = 1
        for purchase in list:
            table.add_row(str(counter), purchase[0], purchase[1])
            counter += 1
            if counter > i:
                break
        console.print(table)

    def input_error(self):
        print('Неверный ввод')

    def exit(self):
        print('Выход из программы')


class View(AbstractView):
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


v = RichView()
m = Model()
c = Controller(m, v)


while True:
    print('\nМеню:')
    print('1. Добавить покупку')
    print('2. Показать все покупки')
    print('3. Показать 5 самых дорогих покупок')
    print('4. Выход')
    print('5. Удалить покупку')

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
    elif choice == '5':
        c.choice_2()
        purchase_num = int(input('Номер покупки, которую нужно удалить: '))
        purchase_index = purchase_num - 1
        c.choice_5(purchase_index)
    else:
        c.view.input_error()