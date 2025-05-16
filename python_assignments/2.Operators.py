# 1. Write a function for arithmetic operators (+, -, *, /)
def arithmetic_operations(a, b):
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)
print("Arithmetic Operations")
a = input("Enter first number: ")
b = input("Enter second number: ")
arithmetic_operations(int(a), int(b))



# 2. Write a method for increment and decrement operators (++ , --)

# Note: Python doesn't have ++ or -- operators. We use +=1 and -=1

def increment_decrement(x):
    print("Original value:", x)
    x += 1
    print("After increment:", x)
    x -= 2
    print("After decrement:", x)
print("Increment and Decrement Operations")
x = input("Enter a number: ")
increment_decrement(int(x))



# 3. Write a program to find the two numbers equal or not

def check_equality(a, b):
    if a == b:
        print(f"{a} and {b} are equal.")
    else:
        print(f"{a} and {b} are not equal.")

print
a = input("Enter first number: ")
b = input("Enter second number: ")
check_equality(int(a), int(b))


# 4. Program for relational operators (<, <=, >, >=)

def relational_ops(x, y):
    print(f"{x} < {y}:", x < y)
    print(f"{x} <= {y}:", x <= y)
    print(f"{x} > {y}:", x > y)
    print(f"{x} >= {y}:", x >= y)
print("Relational Operations")
a = input("Enter first number: ")
b = input("Enter second number: ")
relational_ops(int(a), int(b))


# 5. Print the smaller and larger number

def find_min_max(a, b):
    print("Smaller number:", min(a, b))
    print("Larger number:", max(a, b))

print("Find Min and Max")
a = input("Enter first number: ")
b = input("Enter second number: ")  
find_min_max(int(a), int(b))

 
 
 
 
 
 
  