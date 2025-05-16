# 1. Print “Bright IT Career” ten times using a while loop (instead of range)
print("\n1. Print message 10 times without range:")
count = 0
while count < 10:
    print("Bright IT Career")
    count += 1

# use for loop and range

# print("\n1. Print message 10 times using for loop:")
# for _ in range(10):
#     print("Bright IT Career")

# 2. Print 1 to 20 numbers using while loop
print("\n2. Print 1 to 20 using while loop:")
i = 1
while i <= 20:
    print(i, end=" ")
    i += 1
print()

# 3. Equal and Not Equal operators
print("\n3. Equal and Not Equal check:")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Equal:", a == b)
print("Not Equal:", a != b)

# 4. Print odd and even numbers from 1 to 10 without using range
print("\n4. Odd and Even numbers from 1 to 10:")
num = 1
while num <= 10:
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")
    num += 1

# using for loop and range

# print("\n4. Odd and Even numbers from 1 to 10:")
# for i in range(1, 11):
#     if i % 2 == 0:
#         print(f"{i} is Even")
#     else:
#         print(f"{i} is Odd")


# 5. Largest number among three
print("\n5. Find largest among three numbers:")
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
if x >= y and x >= z:
    print("Largest number is:", x)
elif y >= x and y >= z:
    print("Largest number is:", y)
else:
    print("Largest number is:", z)

# 6. Print even numbers between 10 and 20 using while
print("\n6. Even numbers between 10 and 20:")
i = 10
while i <= 20:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1
print()

# 7. Print 1 to 10 using do-while style logic
print("\n7. Print 1 to 10 using do-while logic:")
i = 1
while True:
    print(i, end=" ")
    i += 1
    if i > 10:
        break
print()

# 8. Armstrong number
print("\n8. Armstrong number check:")
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")

# 9. Prime number check without range
print("\n9. Prime number check:")
num = int(input("Enter a number: "))
if num > 1:
    is_prime = True
    i = 2
    while i * i <= num:
        if num % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")
else:
    print(num, "is not a prime number.")

# using for loop and range

# num = int(input("Enter a number: "))
# if num > 1:
#     for i in range(2, int(num**0.5)+1):
#         if num % i == 0:
#             print(num, "is not a prime number.")
#             break
#     else:
#         print(num, "is a prime number.")
# else:
#     print(num, "is not a prime number.")

# 10. Palindrome check
print("\n10. Palindrome check:")
text = input("Enter a string or number: ")
if text == text[::-1]:
    print(text, "is a palindrome.")
else:
    print(text, "is not a palindrome.")

# 11. Even/Odd using match-case (Python 3.10+)
print("\n11. Even/Odd check using match-case:")
num = int(input("Enter a number: "))
match num % 2:
    case 0:
        print("Even")
    case 1:
        print("Odd")

# 12. Gender detection using switch-style
print("\n12. Gender detection:")
gender = input("Enter M or F: ").upper()
match gender:
    case "M":
        print("Gender: Male")
    case "F":
        print("Gender: Female")
    case _:
        print("Invalid input")
