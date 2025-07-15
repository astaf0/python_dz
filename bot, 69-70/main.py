import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from yandex_gpt import YandexGpt


bot = telebot.TeleBot('')

ya = YandexGpt()


def language_buttons():
    inline_markup = InlineKeyboardMarkup()
    inline_markup.add(InlineKeyboardButton(text='английский 🇬🇧', callback_data='английский'),
                      InlineKeyboardButton(text='немецкий 🇩🇪', callback_data='немецкий'))
    inline_markup.add(InlineKeyboardButton(text='французский 🇫🇷', callback_data='французский'),
                      InlineKeyboardButton(text='итальянский 🇮🇹', callback_data='итальянский'))
    return inline_markup


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Я могу переводить текст на иностранные языки. Выбери язык', reply_markup=language_buttons())


@bot.callback_query_handler(func=lambda callback: callback.data == 'английский')
@bot.callback_query_handler(func=lambda callback: callback.data == 'немецкий')
@bot.callback_query_handler(func=lambda callback: callback.data == 'французский')
@bot.callback_query_handler(func=lambda callback: callback.data == 'итальянский')
def get_language(callback):
    message = callback.message
    bot.edit_message_text(f'Выбран язык: <b>{callback.data}</b>. \nВведи текст, который нужно перевести', message.chat.id, message.id, parse_mode='html')
    ya.language = f'Переведи на {callback.data} язык фразу '


@bot.message_handler()
def get_text(message):
    inline_markup = InlineKeyboardMarkup()
    inline_markup.add(InlineKeyboardButton(text='сменить язык', callback_data='change_language'))
    ya.text = message.text
    request_str = ya.language + ya.text
    bot.send_message(message.chat.id, ya.get_response(request_str), reply_markup=inline_markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'change_language')
def new_language(callback):
    message = callback.message
    bot.edit_message_text('Выбери новый язык', message.chat.id, message.id, reply_markup=language_buttons())


bot.infinity_polling()
