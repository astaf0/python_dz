import json
import os.path
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

token = ''
bot = telebot.TeleBot(token)


class Database:
    def __init__(self):
        self.purchase = None
        self.purchases = self.get_purchases()
        self.buttons = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Добавить покупку'), KeyboardButton('Посмотреть все покупки'))

    def get_purchases(self):
        if os.path.exists('purchases.json'):
            with open('purchases.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        return []

    def save_purchases(self, updated_purchases):
        with open('purchases.json', 'w', encoding='utf-8') as f:
            return json.dump(updated_purchases, f, ensure_ascii=False, indent=4)


db = Database()



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Выбери действие', reply_markup=db.buttons)


@bot.message_handler(func=lambda message: message.text == 'Добавить покупку')
def enter_name(message):
    bot.send_message(message.chat.id, 'Введи название', reply_markup = ReplyKeyboardRemove())
    bot.register_next_step_handler(message, enter_price)


@bot.message_handler(func=lambda message: message.text == 'Посмотреть все покупки')
def see_purchases(message):
    purchases_str = ''
    for i, purchase in enumerate(db.purchases, start=1):
        purchases_str += f'{i}. {purchase['name']} - {purchase['price']} р\n'
    bot.send_message(message.chat.id, purchases_str)


def enter_price(message):
    bot.send_message(message.chat.id, 'Введи цену')
    db.purchase = {'name': message.text}
    bot.register_next_step_handler(message, added_purchase)


def added_purchase(message):
    bot.send_message(message.chat.id, 'Покупка добавлена', reply_markup=db.buttons)
    db.purchase['price'] = message.text
    db.purchases.append(db.purchase)
    db.save_purchases(db.purchases)


bot.infinity_polling()