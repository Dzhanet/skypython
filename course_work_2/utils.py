import json
import random
import requests
from course_work_2.classes import BasicWord


def load_random_word():

    list_of_words = requests.get('https://jsonkeeper.com/b/130X')
    list_of_words = list_of_words.json()

    random.shuffle(list_of_words)
    random_word = list_of_words[0]["word"]
    meaning_for_random_word = list_of_words[0]["subwords"]
    basic_word = BasicWord(random_word, meaning_for_random_word)

    return basic_word
