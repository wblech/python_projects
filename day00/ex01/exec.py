import sys

argc = len(sys.argv)
index = range(argc)
word = ""
for i in index:
    if i != 0:
        word = word + " " + sys.argv[i]
word_reverse = word[::-1]
if argc > 1:
    print(word_reverse.swapcase())
else:
    print("error: No argument")
