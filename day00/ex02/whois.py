import sys

argc = len(sys.argv)
if argc > 2:
    print("Error")
else:
    try:
        nbr = sys.argv[1]
        nbr = int(nbr)
        if nbr == 0:
            print("I'm a zero")
        else:
            result = nbr % 2
            if result:
                print("I'm odd")
            else:
                print("I'm even")
    except TypeError:
        print("Error")
    except IndexError:
        print("")
