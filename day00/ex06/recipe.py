cookbook = {
    "sandwich": {
        'ingredients': ["ham", "bread", "cheese", "tomatoes"],
        'meal': "It is a lunch",
        'prep_time': 10
    },
    "cake": {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': "It is a dessert",
        'prep_time': 60
    },
    "salad": {
        'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': "It is a lunch",
        'prep_time': 15
    }
}


def print_recipe(option):
    message = f"Recipe for {option}:\n\
    Ingredient list: {cookbook[option]['ingredients']}.\n\
    {cookbook[option]['meal']}.\n\
    Takes {cookbook[option]['prep_time']} minutes of cooking."
    print(message)
    print("")
    menu()


def print_cookbook():
    print("List of cookbooks:")
    for key in list(cookbook.keys()):
        print("." + key)
    print("")
    menu()


def add_recipe():
    recipe = input("Please give the recipe's name: ")
    cookbook[recipe] = {}
    cookbook[recipe]['ingredients'] = \
        input("Enter the ingredients(separate by one space): ").split(' ')
    cookbook[recipe]['meal'] = input("Enter the meal's type: ")
    cookbook[recipe]['prep_time'] = input("Preparation time in minutes: ")
    print("")
    menu()


def delete_recipe():
    recipe = input("Please give the recipe's name to be DELETED: ")
    cookbook.pop(recipe)
    print(f"Recipe {recipe} deleted")
    print("")
    menu()


def menu():
    while True:
        option = input("Please select an option by typing the\
corresponding number:\n \
        1: Add a recipe\n \
        2: Delete a recipe\n \
        3: Print a recipe\n \
        4: Print the cookbook\n \
        5: Quit\n")
        print("")
        if not option.isdigit():
            print("This option does not exist, please type the corresponding \
number.\nTo exit, enter 5.\n")
        else:
            option = int(option)
        if option == 1:
            add_recipe()
        elif option == 2:
            delete_recipe()
        elif option == 3:
            recipe = input("Please enter the recipe's name to get \
its details:\n")
            print_recipe(recipe)
        elif option == 4:
            print_cookbook()
        elif option == 5:
            print("Cookbook closed")
            exit()
        else:
            print("This option does not exist, please type the corresponding \
number.\nTo exit, enter 5.\n")


menu()
