class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients,
                 recipe_type, description=None):
        self._listRecipe = ['starter', 'lunch', 'dessert']
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.recipe_type = recipe_type
        self.description = description

    def print_ing(self):
        size = len(self.ingredients)
        txt = ""
        for i, ing in enumerate(self.ingredients):
            if i == size - 1:
                txt += ing + "."
            else:
                txt += ing + ", "
        return txt

    @staticmethod
    def type_error_msg(value, type):
        print(f"Error:\nThe {value} of the recipe must be a {type}")

    @staticmethod
    def empty_error_msg(value):
        print(f"Error:\nThe {value} can´t must not be empty")

    @property
    def name(self):
        try:
            return self._name
        except Exception as error:
            print(error)

    @property
    def cooking_lvl(self):
        return self._cooking_lvl

    @property
    def cooking_time(self):
        return self._cooking_time

    @property
    def ingredients(self):
        return self._ingredients

    @property
    def description(self):
        return self._description

    @property
    def recipe_type(self):
        return self._recipe_type

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
            self.empty_error_msg('name')
        except TypeError:
            self.type_error_msg('name', 'str')

    @cooking_lvl.setter
    def cooking_lvl(self, value):
        try:
            if not value:
                raise ValueError
            elif not(isinstance(value, int)):
                raise TypeError
            elif value not in range(1, 6):
                raise SyntaxError
            else:
                self._cooking_lvl = value
        except ValueError:
            self.empty_error_msg('cookking lvl')
        except TypeError:
            self.type_error_msg('cooking lvl', 'int')
        except SyntaxError:
            print("Error:\n The cooking level must be between 1 - 5")

    @cooking_time.setter
    def cooking_time(self, value):
        try:
            if not value or value < 0:
                raise ValueError
            elif not(isinstance(value, int)):
                raise TypeError
            else:
                self._cooking_time = value
        except ValueError:
            self.empty_error_msg('cooking time')
            print("Cooking time must be a positive number")
        except TypeError:
            self.type_error_msg('cooking time', 'int')

    @ingredients.setter
    def ingredients(self, value):
        try:
            if not value:
                raise ValueError
            elif not(isinstance(value, list)):
                raise TypeError
            else:
                for igr in value:
                    if not(isinstance(igr, str)):
                        raise TypeError
                self._ingredients = value
        except ValueError:
            self.empty_error_msg('ingredients')
        except TypeError:
            self.type_error_msg('ingredients', 'list')
            print("Each ingredient must be a string")

    @description.setter
    def description(self, value):
        try:
            if value is None:
                self._description = value
            elif not(isinstance(value, str)):
                raise TypeError
            else:
                self._description = value
        except TypeError:
            self.type_error_msg('description', 'str')

    @recipe_type.setter
    def recipe_type(self, value):
        try:
            if not value:
                raise ValueError
            elif not(isinstance(value, str)) or value not in self._listRecipe:
                raise TypeError
            else:
                self._recipe_type = value
        except ValueError:
            self.empty_error_msg('recipe type')
        except TypeError:
            self.type_error_msg('recipe type', 'str')
            print(f"The recipe types are {[rec for rec in self._listRecipe]} \
you wrote {value}")

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = f"Recipe: {self.name}\n"\
              f" Cooking Level: {self.cooking_lvl}\n"\
              f" Cooking Time : {self.cooking_time}\n"\
              f" Ingredients  : {self.print_ing()}\n"\
              f" Recipe Type  : {self.recipe_type}\n"\
              f" Description  : {self.description}\n"
        return txt
