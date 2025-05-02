# Задание 1. Класс для общения.
# Создайте класс Chat(), который имеет методы для общения:
# - Hello() – приветствие
# - How() – cпрашивает как дела
# - Buy() – прощается

class Chat():
    def hello(self):
        print('Привет')
    def how(self):
        print('Как дела?')
    def bye(self):
        print('Пока')

Chat().hello()
Chat().how()
Chat().bye()
