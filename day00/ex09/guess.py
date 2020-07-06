from random import randint


def main():
    nbr = randint(1, 99)
    count = 0

    print("This is an interactive guessing game!\n\
You have to enter a number between 1 and 99 to find out the secret \
number.\nType 'exit' to end the game.\n\
Good luck!\n")
    while True:
        guess = input("What's your guess between 1 and 99?\n")
        count += 1
        if guess == "exit":
            print("Goodbye!")
            break
        if not guess.isnumeric():
            print("That's not a number.")
        else:
            guess = int(guess)
            if guess < nbr:
                print("Too low!")
            elif guess > nbr:
                print("Too high!")
            elif guess == nbr:
                if nbr == 42:
                    print("The answer to the ultimate question of life, the \
universe and everything is 42.")
                if count == 1:
                    print("Congratulations! You got it on your first try!")
                else:
                    print("Congratulations, you've got it!\n")
                    print(f"You won in {count} attempts!")
                break


main()
