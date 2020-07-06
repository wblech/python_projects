import sys
import string

morse = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}
argc = len(sys.argv)
index = range(argc)
translated = ""

for i in index:
    if i != 0:
        try:
            phrase = sys.argv[i].lower()
            splitted = phrase.split(' ')
            for t, word in enumerate(splitted):
                if not word.isalnum():
                    raise TypeError
                else:
                    for letter in word:
                        translated += morse[letter] + " "
                if t != len(splitted) - 1:
                    translated += " / "
            if i != argc - 1:
                translated += " / "
        except TypeError:
            translated = "ERROR"
            break

print(translated)
