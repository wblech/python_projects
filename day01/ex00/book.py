from recipe import Recipe
import datetime


class Book:

    def __init__(self, name):
        self.name = name
        self.__create_recipes_list()
        self.__last_update()
        self.__creation_date()

    @property
    def name(self):
        return self._name

    @property
    def recipes_list(self):
        return self._recipes_list

    @property
    def creation_date(self):
        return self._creation_date

    @property
    def last_update(self):
        return self._last_update

    @name.setter
    def name(self, value):
        try:
            if not value:
                raise ValueError
            elif not(isinstance(value, str)):
                raise TypeError
            else:
                self._name = value
        except ValueError:
            print("Error:\nThe book´s name must be informed")
        except TypeError:
            print("Error:\nThe book´s name must be a string")

    def __create_recipes_list(self):
        self._recipes_list = {
            'starter': {},
            'lunch': {},
            'dessert': {}
        }

    def __creation_date(self):
        self._creation_date = datetime.date.today()

    def __last_update(self):
        self._last_update = datetime.date.today()

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        found = 0
        for t in self.recipes_list:
            for n in self.recipes_list[t]:
                if n == name:
                    found = 1
                    print(self.recipes_list[t][n])
        if not(found):
            print(f"Recipe {name} not found")
        return self

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        name_lst = []
        try:
            if recipe_type not in ['starter', 'lunch', 'dessert']:
                raise ValueError
        except ValueError:
            print(f"Error:\nRecipe type expected: starter, lunch, dessert\
\nReceived: {recipe_type}")
        else:
            for name in self.recipes_list[recipe_type]:
                name_lst.append(name)
            return name_lst

    def add_recipe(self, recipe=None):
        """Add a recipe to the book and update last_update"""
        try:
            if recipe is None:
                raise TypeError
            if not(isinstance(recipe, Recipe)):
                raise TypeError
            else:
                self._recipes_list[recipe.recipe_type][recipe.name] = recipe
                self.__last_update()
        except TypeError:
            print("Error:\nThe recipe must be a Recipe instance")
