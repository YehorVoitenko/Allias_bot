import telebot
import config
from telebot import types

bot = telebot.TeleBot("5455678554:AAEqS1e20yR09YkRSC5GDtxvwFD37Gjd0_8")


@bot.message_handler(commands=['start'])
def greeting(message):
    # count = 0
    # bot.send_message(message.chat.id, 'hi, chose you team name:')
    # bot.send_message(message.chat.id, count+1)
    markup = types.ReplyKeyboardMarkup()
    my_name = types.KeyboardButton('name')
    sec_name = types.KeyboardButton('surname')
    markup.add(my_name, sec_name)
    bot.send_message(message.chat.id, 'сайт', reply_markup=markup)

    # random = types.KeyboardButton('randon')


    # if message.text == 'Выбрать случайное название':
    #     bot.send_message(message.chat.id, 'count+1')


# @bot.callback_query_handlers(func=lambda call: True)
# def count1(call, message):
#     count = 0
#     if call.data == 'random':
#         count += 1
#         bot.send_message(message.chat.id, count)


#
# @bot.message_handler(content_types=['text'])
# def echo(message):
#     bot.send_message(message.chat.id, message.text)

# RUN


bot.polling(non_stop=True)
