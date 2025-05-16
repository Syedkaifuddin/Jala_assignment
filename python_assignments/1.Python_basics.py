# 1. Write a program to print your name.
print("My name is Syed Kaifuddin")


# 2. Write a program for a Single line comment and multi-line comments

# This is a single-line comment

'''
This is a multi-line comment.
It can span multiple lines.
Useful for documentation.
'''

print("Comments demonstration complete.")


# 3. Define variables for different Data Types int, Boolean, char, float, double and print on the Console.

my_int = 42               # Integer
my_bool = True            # Boolean
my_char = 'K'             # Character (in Python, a char is just a string of length 1)
my_float = 3.14           # Float
my_double = 99.99999999   # Double (in Python, float covers both float and double precision)

print("Integer:", my_int)
print("Boolean:", my_bool)
print("Character:", my_char)
print("Float:", my_float)
print("Double:", my_double)


# 4. Define the local and Global variables with the same name and print both variables and understand the scope of the variables

x = "Global Variable"

def my_function():
    x = "Local Variable"
    print("Inside function (local x):", x)

my_function()
print("Outside function (global x):", x)

