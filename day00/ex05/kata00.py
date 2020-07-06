t = (19, 42, 21)

size = len(t)
first_part = f"The {size} numbers are"
second_part = ""

for i, nbr in enumerate(t):
    if i != size - 1:
        second_part += str(nbr) + ", "
    else:
        second_part += str(nbr)

print(first_part, second_part)
