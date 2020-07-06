import sys
import string

argc = len(sys.argv)


def format_phrase(phrase):
    table = phrase.maketrans('', '', string.punctuation)
    phrase = phrase.split(' ')
    stripped = [word.translate(table) for word in phrase]
    return stripped


def filter_words(words, size_words):
    for word in reversed(words):
        if len(word) <= size_words:
            words.remove(word)
    return words


try:
    phrase = sys.argv[1]
    if phrase.isnumeric():
        raise IndexError
    size_words = int(sys.argv[2])
    words = format_phrase(phrase)
    words = filter_words(words, size_words)
    print(words)
except (IndexError, ValueError):
    print("ERROR")
