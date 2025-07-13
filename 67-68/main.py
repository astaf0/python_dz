from yandex_gpt import YandexGpt


ya = YandexGpt()

print('Привет!')
for i in range(10):
    q_text = input(f'\nЗадай вопрос {i+1}: ')
    q_role = f'отвечай как {input('Кто будет отвечать? (философ, поэт, друг или др.): ')}'
    print(ya.get_answer(q_text, q_role))

print('\nНельзя задать больше 10 вопросов')