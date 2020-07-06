class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients,
                 recipe_type, description=None):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.recipe_type = recipe_type
        self.description = description

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
            print("ERROR: Name option can't be empty")
        except TypeError:
            print("ERROR: Name must be a string")

    @property
    def cooking_lvl(self):
        try:
            return self._cooking_lvl
        except Exception as error:
            print(error)

    @cooking_lvl.setter
    def cooking_lvl(self, value):
        try:
            if not value:
                raise ValueError
            if type(value) is not int:
                raise TypeError
            if value not in range(1, 6):
                raise SyntaxError
            self._cooking_lvl = value
        except ValueError:
            print("ERROR: Cooking Level option can't be empty")
        except TypeError:
            print("ERROR: Cooking Level must be an integer")
        except SyntaxError:
            print("ERROR: Cooking Level should be between 1 - 5")

    @property
    def cooking_time(self):
        try:
            return self._cooking_time
        except Exception as error:
            print(error)

    @cooking_time.setter
    def cooking_time(self, value):
        try:
            if not value:
                raise ValueError
            if type(value) is not int:
                raise TypeError
            if value < 0:
                raise ValueError
            self._cooking_time = value
        except ValueError:
            print("ERROR: Cooking Time option can't be empty or negative")
        except TypeError:
            print("ERROR: Cooking Time must be an integer")

    @property
    def ingredients(self):
        try:
            return self._ingredients
        except Exception as error:
            print(error)

    @ingredients.setter
    def ingredients(self, value):
        try:
            if not value:
                raise ValueError
            if type(value) is not list:
                raise TypeError
            for ingredient in value:
                if type(ingredient) is not str:
                    raise TypeError
            self._ingredients = value
        except ValueError:
            print("ERROR: Ingredients option can't be empty")
        except TypeError:
            print("ERROR: Ingredients must be a list of strings")

    @property
    def description(self):
        try:
            return self._description
        except Exception as error:
            print(error)

    @description.setter
    def description(self, value):
        try:
            if value is None:
                self._description = value
            elif type(value) is not str:
                raise TypeError
            else:
                self._description = value
        except TypeError:
            print("ERROR: Description must be a strings")

    @property
    def recipe_type(self):
        try:
            return self._recipe_type
        except Exception as error:
            print(error)

    @recipe_type.setter
    def recipe_type(self, value):
        r_type = ("starter", "lunch", "dessert")
        try:
            if not value:
                raise ValueError
            if type(value) is not str:
                raise TypeError
            if value not in r_type:
                raise ValueError
            self._recipe_type = value
        except ValueError:
            print("ERROR: Recipe Type option can't be empty and must be one \
of this options: starter, lunch or dessert")
        except TypeError:
            print("ERROR: Recipe must be a strings")

    def __str__(self):
        """Return the string to print with the recipe info"""
        msg = f"Name: {self.name}\nDescription: {self.description}\n\
Cooking Level: {self.cooking_lvl}/5\nCooking Time: {self.cooking_time} \
minutes\nIngredients: {self.ingredients}\nRecipe Type: {self.recipe_type}"
        return msg
