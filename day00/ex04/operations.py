import sys


if len(sys.argv) > 3:
    print("InputError: too many arguments")
    exit(0)
try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print("Sum: ", a + b)
    print("Difference: ", a - b)
    print("Product: ", a * b)
    print("Quotient: ", a / b)
    print("Remainder: ", a % b)
except IndexError:
    print("Usage: python operations.py\nExample:\n  python operations.py 10 3")
except ValueError:
    print("InputError: only numbers")
except ZeroDivisionError:
    print("Quotient: ERROR (div by zero)")
    print("Remainder: ERROR (div by zero)")
