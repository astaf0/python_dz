import telebot

token = ''
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Начало работы')


@bot.message_handler()
def answers(message):
    if 'привет' in message.text.lower():
        bot.reply_to(message, 'Привет')

    elif 'как' and 'дела' in message.text.lower():
        bot.reply_to(message, 'Нормально')


bot.infinity_polling()

