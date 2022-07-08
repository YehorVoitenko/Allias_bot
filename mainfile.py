import telebot
from telebot import types
import telegram

bot = telebot.TeleBot("5455678554:AAEqS1e20yR09YkRSC5GDtxvwFD37Gjd0_8")


@bot.message_handler(commands=['start'])
def greeting(message):
    markup_inline = types.InlineKeyboardMarkup()
    first = types.InlineKeyboardButton(text='Yes', callback_data='yes')
    sec = types.InlineKeyboardButton(text='No', callback_data='no')
    markup_inline.add(first, sec)
    bot.send_message(message.chat.id, 'Выбери вариант названия', reply_markup=markup_inline)
# @bot.message_handler(commands=['start'])
# def greeting(message):
#     count = 0
#     bot.send_message(message.chat.id, 'привет')
#     markup = types.ReplyKeyboardMarkup()
#     first = types.InlineKeyboardButton(text='name', callback_data='name')
#     # sec = types.KeyboardButton('surname')
#     markup.add(first) # , sec)
#     bot.send_message(message.chat.id, 'сайт', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'yes':
        bot.send_message(call.message.chat.id, 'Выбери')
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        first_id = types.KeyboardButton('первый ID')
        sec_id = types.KeyboardButton('Имя')
        markup_reply.add(first_id, sec_id)
        bot.send_message(call.message.chat.id, 'Нажми на что-то справа снизу', reply_markup=markup_reply)
    elif call.data == 'no':
       pass


@bot.message_handler(content_types=['text'])
def get_text(message):
    if message.text == 'первый ID':
        bot.send_message(message.chat.id, f'Yours id: {message.from_user.id}')
    elif message.text == 'Имя':
        bot.send_message(message.chat.id, f'Yours names: {message.from_user.first_name}')




bot.polling(non_stop=True)