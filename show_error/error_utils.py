from object.button import button
from show_error.show_error_type import error103
from startapp import bot, round_process


def button_ready(message):
    markup_request = button.get_ready_button()
    bot.send_message(message.chat.id, error103)
    msg = bot.send_message(message.chat.id, 'Нажми кнопку \'Готов\'',
                           reply_markup=markup_request, parse_mode='html')
    bot.register_next_step_handler(msg, round_process)