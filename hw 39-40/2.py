# Задание 2. Список дел
# Создайте класс, для работы со списком дела. В качестве хранения дел
# лучше использовать словарь, где ключом делать название дела, а
# значением статус.
# Словарь должен определяться в конструкторе, то есть в методе «init».
# В классе определите методы:
    # - добавить дело
    # Добавить дело в словарь
    # - показать все дела
    # Показать все дела с их статусами
    # - выполнить дело
    # Изменить статус дела на «выполнено»

class Tasks():
    def __init__(self):
        self.todo_list = {}

    def add_task(self, task):
        self.todo_list[task] = 'не выполнено'
        print('дело добавлено')

    def show_tasks(self):
        for key, value in self.todo_list.items():
            print(key, value)

    def complete_task(self, completed_task):
        self.todo_list[completed_task] = 'выполнено'
        self.show_tasks()


tasks = Tasks()

tasks.add_task('отдохнуть')
tasks.add_task('погулять')
tasks.show_tasks()
print('')

tasks.complete_task('погулять')