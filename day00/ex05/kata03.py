phrase = "The right format"

size = len(phrase)

if size < 42:
    print((42 - size) * "-", phrase, sep='', end='')
