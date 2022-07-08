import telebot
from telebot import types

bot = telebot.TeleBot("5455678554:AAEqS1e20yR09YkRSC5GDtxvwFD37Gjd0_8")


@bot.message_handler(commands=['start'])
def greeting(message):
    markup_request = types.ReplyKeyboardMarkup()
    markup_request.add(types.KeyboardButton('Своё название'), types.KeyboardButton('Случайное название'))
    msg = bot.send_message(message.chat.id, "Выбери вариант название", reply_markup=markup_request)
    bot.register_next_step_handler(msg, user_answer)


def user_answer(message):
    if message.text == 'Своё название':
        msg1 = bot.send_message(message.chat.id, "Введите название")
        bot.register_next_step_handler(msg1, user_put_name)
    elif message.text == 'Случайное название':
        bot.send_message(message.chat.id, "Вы выбрали случайное название")


def user_put_name(message):
    team_name = message.text
    bot.send_message(message.chat.id, f'Your name {team_name}')



bot.polling(non_stop=True)

