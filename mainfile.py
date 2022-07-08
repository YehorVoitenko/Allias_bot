
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


@bot.message_handler(content_types=['text'])
def user_answer(message):
    if message.text == 'Своё название':
        msg1 = bot.send_message(message.chat.id, "Введите название")
        bot.register_next_step_handler(msg1, user_put_name)
        types.ReplyKeyboardRemove()
    elif message.text == 'Случайное название':
        with open('names.txt', 'r') as file:
            content = file.read()
            splited = content.split(", ")
            random_name = random.choice(splited)
        bot.send_message(message.chat.id, f"Название первой команды: {random_name}")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        start = types.InlineKeyboardButton('Готов')
        markup.add(start)
        mas = bot.send_message(message.chat.id, f"Команда {random_name} готова начать? Нажми на кнопку, если готов!", reply_markup=markup)


def user_put_name(message):
    team_name = message.text
    bot.send_message(message.chat.id, f'Название первой команды: {team_name}')

def for_vlad(message):
    bot.send_message(message.chat.id, 'Влад красавчик')



bot.polling(non_stop=True)


