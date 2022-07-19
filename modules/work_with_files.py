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


def print_word():
    with open('static/words.txt', 'r') as file:  # Instead of copying funcs - use class or another file; decorators
        content = file.read()
        splited = content.split("\n")
        word = random.choice(splited)
    return word