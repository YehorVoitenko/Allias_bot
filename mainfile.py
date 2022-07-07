import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands = ['start'])
def give_frog(message):
    sti = open(r'E:\FirstTeleBot\Allias_bot\frog.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, "Чел, дарова блин, {0.first_name}! это я {1.first_name}. "
                                     "Это так, просто учусь пока, ничё интересного". format(message.from_user, bot.get_me()),
                     parse_mode='html')

@bot.message_handler(content_types= ['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)

# RUN
bot.polling(non_stop=True)
