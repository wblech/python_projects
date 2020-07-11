import os
import math


def generator(text, sep=" ", option=None):
    '''Option is an optional arg, sep is mandatory'''
    try:
        if not isinstance(text, str):
            raise Exception
        words = text.split(sep)
        if option is not None:
            if option == "shuffle":
                words = __shuffle(words)
            elif option == "unique":
                words = list(dict.fromkeys(words))
                print(words)
            elif option == "ordered":
                words.sort(words)
            else:
                raise Exception
    except Exception:
        print("Error")
    else:
        for word in words:
            yield word


def __shuffle(list):
    # Fisher-Yates Shuffle
    """Gets random sequence of integers from /dev/urandom UNIX device.
    This function is an implementation of the Durstenfeld version of
    the Fisher-Yates shuffle algorthm. To get the random indexes, it
    reads a certain number of bytes from /dev/urandom. As such, the
    behavior on non-Linux systems is unknown. To get a more precise
    randomness for long lists, it reads n bytes according to the list
    size (e.g. 1 byte readed for lists with less than 256 elements, 2
    bytes for lists with less than 65536 elements, and so on). For more
    details regarding the algorithm, access its Wikipedia page:
    https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
    Space Complexity    -> O(1)
    Time Complexity     -> O(n)
    """
    list_len = len(list)
    n_bytes = math.ceil(math.log(list_len, 2) / 8)
    while list_len - 1:
        random_nbr = int.from_bytes(os.urandom(n_bytes), "big") % list_len
        tmp = list[list_len - 1]
        list[list_len - 1] = list[random_nbr]
        list[random_nbr] = tmp
        list_len -= 1
    return list




text = "Le Lorem Ipsum est simplement du faux texte."
for word in generator(text, sep=" ", option="unique"):
    print(word)
