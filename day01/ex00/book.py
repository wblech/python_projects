from pyrecipe import Recipe
import datetime


class Book():
    def __init__(self, name):
        self.name = name
        self.__create_recipes_list()
        self.__last_update()
        self.__creation_date()

    @property
    def name(self):
        try:
            return self._name
        except Exception as error:
            print(error)

    @name.setter
    def name(self, value):
        try:
            if not value:
                raise ValueError
            if type(value) is not str:
                raise TypeError
            self._name = value
        except ValueError:
            print("ERROR: Book name option can't be empty")
        except TypeError:
            print("ERROR: Book name must be a string")

    @property
    def recipes_list(self):
        return self._recipes_list

    def __create_recipes_list(self):
        self._recipes_list = {
            "starter": {},
            "lunch": {},
            "dessert": {}
        }

    @property
    def creation_date(self):
        return self._creation_date

    def __creation_date(self):
        self._creation_date = datetime.date.today()

    @property
    def last_update(self):
        return self._last_update

    def __last_update(self):
        self._last_update = datetime.date.today()

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        self._recipes_list[recipe.recipe_type][recipe.name] = recipe
        self.__last_update()

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        self._found = 0
        for t in self.recipes_list:
            for n in self.recipes_list[t]:
                if n == name:
                    self._found = 1
                    print(self.recipes_list[t][n])
        if self._found == 0:
            print(f"Recipe {name} not found")

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        try:
            if recipe_type not in ["starter", "lunch", "dessert"]:
                raise ValueError
        except ValueError:
            print(f"ERROR:\nRecipe type excepected: starter,\
lunch, dessert\nReceived: {recipe_type}")
        else:
            for name in self.recipes_list[recipe_type]:
                print(self.recipes_list[recipe_type][name])
                print()
