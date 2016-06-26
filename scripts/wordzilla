from __future__ import print_function
import sqlite3
import os
import argparse
import re
import textwrap
from functools import wraps

__all__ = ['get_meanings', 'check_word']
__version__ = '1.0'
__author__ = 'Karthikeyan <tir.karthi@gmail.com>'

db_path = os.path.expanduser("~/Wordzilla")
db = sqlite3.connect(db_path)

text_wrapper = textwrap.TextWrapper()
text_indent = ' ' * 4
text_wrapper.initial_indent = text_indent
text_wrapper.subsequent_indent = text_indent

color = {
    'green' : '\033[92m',
    'red' : '\033[91m'
    }

parts_of_speech = ('noun', 'pronoun', 'adjective',
                   'verb', 'adverb', 'preposition',
                   'conjunction', 'interjection', 'determiner', 'default_part_of_speech')


parser = argparse.ArgumentParser()

parser.add_argument("-n", "--number_of_meanings", type=int,
                    default=5, action="store", dest="number_of_meanings",
                    help="number of meanings to be returned")

parser.add_argument("-c", "--color",
                    default=False, action="store_true", dest="colored_output",
                    help="add color to output")

parser.add_argument("-p",
                    default='default_part_of_speech', dest="part_of_speech",
                    choices=parts_of_speech,
                    help="filter meaning by part of speech")

parser.add_argument('words', nargs=argparse.REMAINDER)

options = parser.parse_args()

args = []
if options.words:
    args = options.words[0]

def colored_output(color):
    def colored_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            text = ''.join(args)
            if options.colored_output:
                func(color + text)
            else:
                func(text)
        return wrapper
    return colored_decorator


def check_word(word):
    """Check if the word contains only alphabets
    """

    word = word.strip().lower()

    return bool(re.match(r'^[a-z]+$', word))

def get_meanings(word='man', part_of_speech='', number_of_meanings=5):
    """"Get the meanings for the word and return a generator.
    Yield part of speech and the meaning for each iteration.
    Filter the meanings as per the part of speech option if present.
    """

    cur = db.cursor()
    word = word.lower()
    table = word[0]

    if part_of_speech:
        part_of_speech = part_of_speech.lower().capitalize()
        query = "select part, meaning from " + table + " where word=? and part = ?"
        meanings = cur.execute(query, (word, part_of_speech))
    else:
        query = "select part, meaning from " + table + " where word=? "
        meanings = cur.execute(query, (word, ))

    while True:
        try:
            part_of_speech, meaning = meanings.next()
            if number_of_meanings:
                yield part_of_speech, meaning
                number_of_meanings -= 1
            else:
                raise StopIteration
        except StopIteration:
            meanings.close()
            break

def get_word():
    if args:
        word = args
    else:
        word = raw_input("Enter a word : ")

    return word

def print_part_of_speech_and_meaning(part_of_speech, meaning):
    """Print the part of speech and meaning.
    """

    print_part_of_speech(part_of_speech)
    print_meaning(meaning)

@colored_output(color['red'])
def print_part_of_speech(part_of_speech):
    """Colorise the part of speech if the option is present.
    Defaults to red.
    """

    print(part_of_speech)

@colored_output(color['green'])
def print_meaning(meaning):
    """Colorise the part of speech if the option is present.
    Defaults to green.
    """

    print('\n'.join(text_wrapper.wrap(meaning)) + "\n")

if __name__ == "__main__":
    word = get_word()

    if word:
        if check_word(word):

            part_of_speech = options.part_of_speech.lower().capitalize()
            if part_of_speech == "Default_part_of_speech":
                part_of_speech = ''

            number_of_meanings = options.number_of_meanings

            meanings = get_meanings(word, part_of_speech, number_of_meanings)

            no_words_found = True

            for part_of_speech, meaning in meanings:
                print_part_of_speech_and_meaning(part_of_speech, meaning)
                no_words_found = False

            if no_words_found:
                print("No meanings found")
        else:
            print("Please enter a word without any hypens or special symbols")
    else:
        print("Please enter a word")
    db.close()
