import string


def text_analyzer(text=None):
    """This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text."""
    text_size = 0
    uc_count = 0
    lc_count = 0
    pun_count = 0
    spa_count = 0

    while not text:
        text = input("Please inform a text: ")
    text_size = len(text)
    for letter in text:
        if letter.isupper():
            uc_count += 1
        elif letter.islower():
            lc_count += 1
        elif letter.isspace():
            spa_count += 1
        elif letter in string.punctuation:
            pun_count += 1
    message = (
        f"The text contains {text_size} characters:\n"
        f"- {uc_count} upper letters\n"
        f"- {lc_count} lower letters\n"
        f"- {pun_count} punctuation marks\n"
        f"- {spa_count} spaces\n"
    )
    print(message)
