import random
import json
from constants.path import ADJECTIVES, NOUN, WORDS_FOR_GAME, RU_TRANSLATIONS
from models.get_bot_phrase import Translation


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


def get_translation(file: str = RU_TRANSLATIONS):
    with open(file, encoding='utf_8_sig') as text:
        kwargs = json.load(text)
    return Translation(**kwargs)
