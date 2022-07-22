import random
import telebot
from settings.config import config
from file_utils.file_path.get_file_path import ADJECTIVES, NOUN, WORDS_FOR_GAME

bot = telebot.TeleBot(config.TOKEN)


def get_random_name():
    with open(ADJECTIVES, 'r') as file:
        content = file.read()
        separate = content.split("\n")
        first_random = random.choice(separate)

    with open(NOUN, 'r') as file:
        content = file.read()
        separate = content.split("\n")
        second_random = random.choice(separate)
    return f'{first_random} {second_random}'


def give_word_for_round():
    with open(WORDS_FOR_GAME, 'r') as file:
        content = file.read()
        separate = content.split("\n")
        word = random.choice(separate)
    return word
