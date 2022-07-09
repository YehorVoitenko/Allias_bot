import telebot
import random
from telebot import types
import text_redactor

bot = telebot.TeleBot("5455678554:AAEqS1e20yR09YkRSC5GDtxvwFD37Gjd0_8")


@bot.message_handler(commands=['start'])
def greeting(message):
    markup_request = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup_request.add(types.InlineKeyboardButton('Своё название'), types.InlineKeyboardButton('Случайное название'))
    msg = bot.send_message(message.chat.id, "Выбери вариант названия", reply_markup=markup_request)
    bot.register_next_step_handler(msg, user_answer)


def user_answer(message):
    if message.text == 'Своё название':
        msg1 = bot.send_message(message.chat.id, "Введите название")
        bot.register_next_step_handler(msg1, are_you_ready_own)
    elif message.text == 'Случайное название':
        with open('names.txt', 'r') as file:
            content = file.read()
            splited = content.split(", ")
            random_name = random.choice(splited)
        msg2 = bot.send_message(message.chat.id, f"Название первой команды: <b><u>{random_name}</u></b>", parse_mode='html')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        start = types.InlineKeyboardButton('Готов')
        markup.add(start)
        bot.send_message(message.chat.id, f"Команда <b><u>{random_name}</u></b> готова начать? Нажми на кнопку, если готов!",
                         reply_markup=markup, parse_mode='html')


def are_you_ready_own(message):
    team_name = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start = types.InlineKeyboardButton('Готов')
    markup.add(start)
    bot.send_message(message.chat.id, f"Команда <b>{team_name}</b> готова начать? Нажми на кнопку, если готов!", reply_markup=markup, parse_mode='html')



bot.polling(non_stop=True)
