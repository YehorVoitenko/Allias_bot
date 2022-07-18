import random


def output_random_name():
    with open('static/nouns.txt', 'r') as file:  # Instead of copying funcs - use class or another file; decorators
        content = file.read()
        splited = content.split("\n")
        nouns = random.choice(splited)

    with open('static/adjectives.txt', 'r') as file:  # Instead of adjectives.txt - use file with adjectives
        content = file.read()
        splited = content.split("\n")
        adjectives = random.choice(splited)
    return f'{adjectives} {nouns}'


def show_word():
    with open('static/words.txt', 'r') as file:  # Instead of copying funcs - use class or another file; decorators
        content = file.read()
        splited = content.split("\n")
        word = random.choice(splited)
    return f'{word}'
    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    # markup.add(types.InlineKeyboardButton(text='+', callback_data='plus'),
    #            types.InlineKeyboardButton(text='-', callback_data='minus'))
    # msg = bot.send_message(message.chat.id, f'<b>{word}</b>', reply_markup=markup, parse_mode='html')
    # bot.register_next_step_handler(msg, plus_or_minus)
