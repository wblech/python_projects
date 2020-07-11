# Projects for Practicing Python OOP

Some projects ideas that I did for learning python OOP

## Exercise 00 - The Book

You will provide a test.py file to test your classes and prove that they are working the right way.
You can import all the classes into your test.py file by adding these lines at the top of the test.py file:

```python
from book import Book
from recipe import Recipe
```

You will have to make a class Book and a class Recipe
Let’s describe the Recipe class. It has some attributes:

• name (str)

• cooking_lvl (int) : range 1 to 5

• cooking_time (int) : in minutes (no negative numbers)

• ingredients (list) : list of all ingredients each represented by a string

• description (str) : description of the recipe

• recipe_type (str) : can be “starter”, “lunch” or “dessert”.

You have to initialize the object Recipe and check all its values, only the description can be empty.
In case of input errors, you should print what they are and exit properly.
You will have to implement the built-in method __str__.
It’s the method called when you execute this code:

```python
tourte = Recipe(...)
to_print = str(tourte)
print(to_print)
```

It’s implemented this way:

```python
def __str__(self):
"""Return the string to print with the recipe info"""
txt = ""
"""Your code goes here"""
return txt
```

The Book class also has some attributes:

• name (str)

• last_update (datetime)

• creation_date (datetime)

• recipes_list (dict) : a dictionnary why 3 keys: “starter”, “lunch”, “dessert”.

You will have to implement some methods in Book:

```python
def get_recipe_by_name(self, name):
"""Print a recipe with the name `name` and return the instance"""
pass
def get_recipes_by_types(self, recipe_type):
"""Get all recipe names for a given recipe_type """
pass
def add_recipe(self, recipe):
"""Add a recipe to the book and update last_update"""
pass
```

You will have to handle the error if the arg passed in add_recipe is not a Recipe.

## Exercise 01 - Family tree

You will have to make a class and its children.
Create a GotCharacter class and initialize it with the following attributes:

• first_name

• is_alive (by default is True)

Pick up a GoT House (e.g., Stark, Lannister. . . ). Create a child class that inherits from GotCharacter and
define the following attributes:

• family_name (by default should be the same as the Class)

• house_words (e.g., the House words for the Stark House is: “Winter is Coming”)

Example:

```python
class Stark(GotCharacter):
def __init__(self, first_name=None, is_alive=True):
super().__init__(first_name=first_name, is_alive=is_alive)
self.family_name = "Stark"
self.house_words = "Winter is Coming"
```

Add two methods to your child class:

• print_house_words: prints to screen the House words

• die: changes the value of is_alive to False

Running commands in the Python console, an example of what you should get:

```python
> python
>>> from game import GotCharacter, Stark
>>> arya = Stark("Arya")
>>> print(arya.__dict__)
{'first_name': 'Arya', 'is_alive': True, 'family_name': 'Stark', 'house_words': 'Winter is
,! Coming'}
>>> arya.print_house_words()
Winter is Coming
>>> print(arya.is_alive)
True
>>> arya.die()
>>> print(arya.is_alive)
False
```

You can add any attribute or method you need to your class and format the docstring the way you want to.
Feel free to create other children of GotCharacter.

```python
>>> print(arya.__doc__)
A class representing the Stark family. Or when bad things happen to good people.
```

## Ex02 - The Vector

forbidden: Numpy

You will provide a testing file to prove that your class works as expected.
You will have to create a helpful class, with more options and providing enhanced ease of use for the user.
In this exercise, you have to create a Vector class. The goal is to have vectors and be able to perform
mathematical operations with them.

```python
>> v1 = Vector([0.0, 1.0, 2.0, 3.0])
>> v2 = v1 * 5
>> print(v2)
(Vector [0.0, 5.0, 10.0, 15.0])
```

It has 2 attributes:

• values : list of float

• size : size of the vector -> Vector([0.0, 1.0, 2.0, 3.0]).size == 4

You should be able to initialize the object with:

• a list of floats: Vector([0.0, 1.0, 2.0, 3.0])

• a size Vector(3) -> the vector will have values = [0.0, 1.0, 2.0]

• a range or Vector((10,15)) -> the vector will have values = [10.0, 11.0, 12.0, 13.0, 14.0]

You will implement all the following built-in functions (called ‘magic methods’) for your Vector class:

```python
__add__
__radd__
# add : scalars and vectors, can have errors with vectors.
__sub__
__rsub__
# sub : scalars and vectors, can have errors with vectors.
__truediv__
__rtruediv__
# div : only scalars.
__mul__
__rmul__
# mul : scalars and vectors, can have errors with vectors,
# return a scalar if we perform Vector * Vector (dot product)
```

### Vectors authorized operations are:

• Addition between two vectors of same dimension (m * 1)

• Substraction between two vectors of same dimension (m * 1)

• Multiplication and division between one vector (m * 1) and one scalar (1 * 1)	

• Mutiplication between two vectors of same dimensons (m * 1)

Don’t forget to handle all kind of errors properly!

## Ex 03 - The Matrix

forbidden: Numpy

You will provide a testing file to prove that your class works as expected.
You will have to create a helpful class, with more options and providing enhanced ease of use for the user.
In this exercise, you have to create a Matrix class. The goal is to have matrices and be able to perform both
matrix-matrix operation and matrix-vector operations with them.

```python
>> m1 = Matrix([[0.0, 1.0, 2.0, 3.0],
[0.0, 2.0, 4.0, 6.0]])
>> m2 = Matrix([[0.0, 1.0],
[2.0, 3.0],
[4.0, 5.0],
[6.0, 7.0]])
>> print(m1 * m2)
(Matrix [[28., 34.], [56., 68.]])
```
It has 2 attributes:
• data : list of lists -> the elements stored in the matrix
• shape : by shape we means the dimensions of the matrix as a tuple (rows, columns) -> Matrix([[0.0,
1.0], [2.0, 3.0], [4.0, 5.0]]).shape == (3, 2)
You should be able to initialize the object with:
• the elements of the matrix as a list of lists: Matrix([[0.0, 1.0, 2.0, 3.0], [4.0, 5.0, 6.0, 7.0]])
-> the dimensions of this matrix are then (2, 4)
• a shape Matrix((3, 3)) -> the matrix will be filled by default with zeroes
• the expected elements and shape Matrix([[0.0, 1.0, 2.0], [3.0, 4.0, 5.0], [6.0, 7.0, 8.0]],
(3, 3))
You will implement all the following built-in functions (called ‘magic methods’) for your Matrix class:

```python
__add__
__radd__
# add : vectors and matrices, can have errors with vectors and matrices.
__sub__
__rsub__
# sub : vectors and matrices, can have errors with vectors and matrices.
__truediv__
__rtruediv__
# div : only scalars.
__mul__
__rmul__
# mul : scalars, vectors and matrices , can have errors with vectors and matrices,
# return a Vector if we perform Matrix * Vector (dot product)
__str__
__repr__
```

### Matrix - vector authorized operations are:

• Multiplication between a (m * n) matrix and a (n * 1) vector - Not implemented yet

### Matrix - matrix authorized operations are:

• Addition between two matrices of same dimension (m * n)

• Substraction between two matrices of same dimension (m * n)

• Multiplication or division between one matrix (m * n) and one scalar (1 * 1) - Not implemented yet

• Mutiplication between two matrices of compatible dimension: (m * n) and (n * p)

##Ex04 - Generator!

forbidden func: random

Code a function called generator that takes a text as input, uses the string sep as a splitting parameter, and
yields the resulting substrings.
The function can take an optional argument.
The options are:

• “shuffle”: shuffle the list of words.

• “unique”: return a list where each word appears only once.

• “ordered”: alphabetically sort the words.

```python
# function prototype
def generator(text, sep=" ", option=None):
'''Option is an optional arg, sep is mandatory'''
```

You can only call one option at a time.

```python
>> text = "Le Lorem Ipsum est simplement du faux texte."
>> for word in generator(text, sep=" "):
... print(word)
...
Le
Lorem
Ipsum
est
simplement
du
faux
texte.
>> for word in generator(text, sep=" ", option="shuffle"):
... print(word)
...
simplement
texte.
est
faux
Le
Lorem
Ipsum
du
>> for word in generator(text, sep=" ", option="ordered"):
... print(word)
...
Ipsum
Le
Lorem
du
est
faux
simplement
texte.
```

The function should return “ERROR” one time if the text argument is not a string, or if the option argument
is not valid.

##Ex05 - Working with lists

forbidden: while

Code a class Evaluator, that has two static functions named: zip_evaluate and enumerate_evaluate.
The goal of these 2 functions is to compute the sum of the lengths of every words of a given list weighted by a
list a coefs.
The lists coefs and words have to be the same length. If this is not the case, the function should return -1.
You have to obtain the desired result using zip in the zip_evaluate function, and with enumerate in the
enumerate_evaluate function.

```python
>> from eval import Evaluator
>>
>> words = ["Le", "Lorem", "Ipsum", "est", "simple"]
>> coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
>> Evaluator.zip_evaluate(coefs, words)
32.0
>> words = ["Le", "Lorem", "Ipsum", "n'", "est", "pas", "simple"]
>> coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
>> Evaluator.enumerate_evaluate(coefs, words)
-1
```
