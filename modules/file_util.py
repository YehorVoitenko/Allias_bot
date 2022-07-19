import random


def create_random_name():
    with open('static/team_name_words/nouns.txt', 'r') as file:
        content = file.read()
        splited = content.split("\n")
        nouns = random.choice(splited)

    with open('static/team_name_words/adjectives.txt', 'r') as file:
        content = file.read()
        splited = content.split("\n")
        adjectives = random.choice(splited)
    return f'{adjectives} {nouns}'


def print_word():
    with open('static/game_words/words.txt', 'r') as file:
        content = file.read()
        splited = content.split("\n")
        word = random.choice(splited)
    return word