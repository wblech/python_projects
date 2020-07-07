# Projects for Practicing Python

Some projects ideas that I did for learning python

## Ex00

Find the commands to:

1. Output a list of installed packages.
2. 2. Output a list of installed packages and their versions.
3. Show the package metadata of numpy.
4. Search for PyPI packages whose name or summary contains “tesseract”.
5. Freeze the packages and their current versions in a requirements.txt file you have to turn-in.

## Ex1

You will have to make a program that reverses the order of a string and the case of its words.
If we have more than one argument we have to merge them into a single string and separate each arg by a ’ ’
(space char).

```python
> python exec.py "Hello World!" | cat -e
!DLROw OLLEh$
> python exec.py "Hello" "my Friend" | cat -e
DNEIRf YM OLLEh$
> python exec.py
>
```

## Ex02 - The Odd, the Even and the Zero

You will have to make a program that checks if a number is odd, even or zero.
The program will accept only one parameter, an integer.

```python
> python whois.py 12
I'm Even.
> python whois.py 3
I'm Odd.
> python whois.py
> python whois.py 0
I'm Zero.
> python whois.py Hello
ERROR
> python whois.py 12 3
ERROR
```

## Ex03 - Functional file

Create a function called text_analyzer that displays the sums of upper-case characters, lower-case characters,
punctuation characters and spaces in a given text.
text_analyzer will take only one parameter: the text to analyze. You have to handle the case where the text is
empty (maybe by setting a default value). If there is no text passed to the function, the user is prompted to give
one.
Test it in the Python console:

```python
> python
>>> from count import text_analyzer
>>> text_analyzer("Python 2.0, released 2000, introduced
features like List comprehensions and a garbage collection
system capable of collecting reference cycles.")
The text contains 143 characters:
- 2 upper letters
- 113 lower letters
- 4 punctuation marks
- 18 spaces
>>> text_analyzer("Python is an interpreted, high-level,
general-purpose programming language. Created by Guido van
Rossum and first released in 1991, Python's design philosophy
emphasizes code readability with its notable use of significant
whitespace.")
The text contains 234 characters:
- 5 upper letters
- 187 lower letters
- 8 punctuation marks
- 30 spaces
>>> text_analyzer()
What is the text to analyse?
>> Python is an interpreted, high-level, general-purpose
programming language. Created by Guido van Rossum and first
released in 1991, Python's design philosophy emphasizes code
readability with its notable use of significant whitespace.
The text contains 234 characters:
- 5 upper letters
- 187 lower letters
- 8 punctuation marks
- 30 spaces
```

Handle the case when more than one parameter is given to text_analyzer:

```python
>>> from count import text_analyzer
>>> text_analyzer("Python", "2.0")
ERROR
```
You’re free to write your docstring and format it the way you want.

```python
>>> print(text_analyzer.__doc__)
This function counts the number of upper characters, punctuation and spaces in a given text.
```
## Ex04 - Elementary

You will have to make a program that prints the results of the four elementary mathematical operations
of arithmetic (addition, subtraction, multiplication, division) and the modulo operation. This should be
accomplished by writing a function that takes 2 numbers as parameters and returns 5 values, as formatted in
the console output below.

```python
Sum: 13
Difference: 7
Product: 30
Quotient: 3.3333333333333335
Remainder: 1
>>
python operations.py 42 10
Sum: 52
Difference: 32
Product: 420
Quotient: 4.2
Remainder: 2
>>
python operations.py 1 0
Sum: 1
Difference: 1
Product: 0
Quotient: ERROR (div by zero)
Remainder: ERROR (modulo by zero)
>>
python operations.py
Usage: python operations.py <number1> <number2>
Example:
python operations.py 10 3
>>
python operations.py 12 10 5
InputError: too many arguments
Usage: python operations.py <number1> <number2>
Example:
python operations.py 10 3
>>
python operations.py "one" "two"
InputError: only numbers
Usage: python operations.py <number1> <number2>
Example:
python operations.py 10 3
>>
python operations.py "512" "63.1"
InputError: only numbers
Usage: python operations.py <number1> <number2>
Example:
python operations.py 10 3
```

## Ex05 - The right format

Let’s get familiar with the useful concept of string formatting through a kata series.

### kata00

```python
t = (19,42,21)
```

Including the tuple above in your file, write a program that dynamically builds up a formatted string like the
following

```python
> python kata00.py
The 3 numbers are: 19, 42, 21
```

### kata01
```python
languages = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}
```
Using the languages dictionary above, a similar exercise:
```python
> python kata01.py
Python was created by Guido van Rossum
Ruby was created by Yukihiro Matsumoto
PHP was created by Rasmus Lerdorf
```
### kata02
```python
(3,30,2019,9,25)
```
Given the tuple above, whose values stand for: (hour, minutes, year, month, day), write a program that
displays it in the following format:
```python
> python kata02.py
09/25/2019 03:30
```

### kata03
phrase = "The right format"
Write a program to display the string above right-aligned with ‘-’ padding and a total length of 42 characters:
```python
> python kata03.py | cat -e
--------------------------The right format%
> python kata03.py | wc -c
42
```
### kata04
```python
( 0, 4, 132.42222, 10000, 12345.67)
```
Given the tuple above, return the following result:
```python
> python kata04.py
day_00, ex_04 : 132.42, 1.00e+04, 1.23e+04
```
## Ex06 - A recipe

It is time to discover Python dictionaries. Dictionaries are collections that contain mappings of unique keys to
values.
Hint: check what is a nested dictionary in Python.
First, you will have to create a cookbook dictionary called cookbook.
cookbook will store 3 recipes:
• sandwich
• cake
• salad
Each recipe will store 3 values:
• ingredients: a list of ingredients
• meal: type of meal
• prep_time: preparation time in minutes
Sandwich’s ingredients are ham, bread, cheese and tomatoes. It is a lunch and it takes 10 minutes of preparation.
Cake’s ingredients are flour, sugar and eggs. It is a dessert and it takes 60 minutes of preparation.
Salad’s ingredients are avocado, arugula, tomatoes and spinach. It is a lunch and it takes 15 minutes of
preparation.
1. Get to know dictionaries. In the first place, try to print only the keys of the dictionary. Then only the
values. And to conclude, all the items.
2. Write a function to print a recipe from cookbook. The function parameter will be: name of the recipe.
3. Write a function to delete a recipe from the dictionary. The function parameter will be: name of the recipe.
4. Write a function to add a new recipe to cookbook with its ingredients, its meal type and its preparation
time. The function parameters will be: name of recipe, ingredients, meal and prep_time.
5. Write a function to print all recipe names from cookbook. Think about formatting the output.
6. Last but not least, make a program using the four functions you just created. The program will prompt the
user to make a choice between printing the cookbook, printing only one recipe, adding a recipe, deleting a
recipe or quitting the cookbook.
It could look like the example below but feel free to organize it the way you want to:

```python
> python recipe.py
Please select an option by typing the corresponding number:
1: Add a recipe
2: Delete a recipe
3: Print a recipe
4: Print the cookbook
5: Quit
>> 3
Please enter the recipe's name to get its details:
>> cake
Recipe for cake:
Ingredients list: ['flour', 'sugar', 'eggs']
To be eaten for dessert.
Takes 60 minutes of cooking.
```

Your program must continue running until the user exits it (option 5):

```python
> python recipe.py
Please select an option by typing the corresponding number:
1: Add a recipe
2: Delete a recipe
3: Print a recipe
4: Print the cookbook
5: Quit
>> 5
Cookbook closed.
```

The program will also continue running if the user enters a wrong value. It will prompt the user again until the
value is correct:


```python
> python recipe.py
Please select an option by typing the corresponding number:
1: Add a recipe
2: Delete a recipe
3: Print a recipe
4: Print the cookbook
5: Quit
>> test
This option does not exist, please type the corresponding number.
To exit, enter 5.
>>
```
## Ex07 - Shorter, faster, pythonest

Using list comprehensions, you will have to make a program that removes all the words in a string that are
shorter than or equal to n letters, and returns the filtered list with no punctuation.
The program will accept only two parameters: a string, and an integer n.

```python
> python filterwords.py "Hello, my friend" 3
['Hello', 'friend']
> python filterwords.py "A robot must protect its own existence as long as such protection
,! does not conflict with the First or Second Law" 6
['protect', 'existence', 'protection', 'conflict']
> python filterwords.py Hello World
ERROR
> python filterwords.py 300 3
ERROR
```
## Ex08 - S.O.S

You will have to make a function which encodes strings into Morse code.
The input will accept all alphanumeric characters.

```python
> python sos.py "SOS"
... --- ...
> python sos.py
> python sos.py "HELLO / WORLD"
ERROR
> python sos.py "96 BOULEVARD" "Bessiere"
----. -.... / -... --- ..- .-.. . ...- .- .-. -.. / -... . ... ... .. . .-. .
```
## Ex09 - Secret number

You will have to make a program that will be an interactive guessing game. It will ask the user to guess a
number between 1 and 99. The program will tell the user if their input is too high or too low. The game ends
when the user finds out the secret number or types exit.
You will have to import the random module with the randint function to get a random number. You have to
count the number of trials and print that number when the user wins.

```python
> python guess.py
This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!
What's your guess between 1 and 99?
>> 54
Too high!
What's your guess between 1 and 99?
>> 34
Too low!
What's your guess between 1 and 99?
>> 45
Too high!
What's your guess between 1 and 99?
>> A
That's not a number.
What's your guess between 1 and 99?
>> 43
Congratulations, you've got it!
You won in 5 attempts!
```

If the user discovers the secret number on the first try, tell them. Bonus: if the secret number is 42, make a
reference to Douglas Adams.


```python
> python guess.py
What's your guess between 1 and 99?
>> 42
The answer to the ultimate question of life, the universe and everything is 42.
Congratulations! You got it on your first try!
```
Other example:

```python
> python guess.py
This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!
What's your guess between 1 and 99?
>> exit
Goodbye!
```
