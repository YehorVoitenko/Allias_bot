from object import button
from startapp import bot, get_round_time
from utils.file_utils import get_translation

bot_phrase = get_translation()


def button_ready(message):
    markup_request = button.get_ready_button()
    bot.send_message(message.chat.id, bot_phrase.error103)
    msg = bot.send_message(message.chat.id, bot_phrase.button_ready,
                           reply_markup=markup_request, parse_mode='html')
    bot.register_next_step_handler(msg, get_round_time)
