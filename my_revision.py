# My revision for python code.
# it contains examples of f strings, functions, etc.  

# f string example:

# name = "Sonal"
# age = 24
# print(f"Hi I'm {name}. I'm {age} years old.")

# FUNCTIONS EXAMPLES

# def greet():
    
#     name = "John"
#     age = 23

#     def game(age,name):
#         if age > 18:
#             print(f"Hi {name}. You are an adult. You can play this game!")
#         else:
#             print(F"Hi {name}. You are not adult. You can't play this game!")
        
#         return "Game Over"
#     game(age,name)
    
# greet()

# def greet():
#     name = "John"
#     age = 23

#     def game(age, name):
#         if age > 18:
#             print(f"Hi {name}. You are an adult. You can play this game!")
#         else:
#             print(f"Hi {name}. You are not an adult. You can't play this game!")
        
#         return "Game Over"  # Yeh return statement hai, jo function ke end par value return karega

#     # Calling the game function and printing the return value
#     result = game(age, name)  # Function call se return value ko result variable me store kiya
#     print(result)  # Print the returned value

# greet()

# 🔹 Level 1: Basic Function Practice

# Write a function to add two numbers.

def add(a, b):
    return a + b
print(add(5,10))


# Write a function that returns whether a number is even or odd.

def is_even_or_odd(num):
    if num % 2 == 0:
        return f"{num} is even"
    else:
        return f"{num} is odd"
    
# print(is_even_or_odd(10)) 
# or we can store the result in a variable and print it later
result = is_even_or_odd(10)
print(result)

# Write a function that takes a name and prints a greeting.

def greet(name):
    return f"Hello, {name}!"

print(greet("Sonal"))

# Write a function to find the factorial of a number.
def fact(n):
   if n ==0 or n == 1:
       return 1
   else:
       return n*fact(n-1)
print(fact(5))


# Write a function to return the maximum of three numbers.
def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
print(max_of_three(10, 20,30))

# Write a function that returns the square and cube of a number.
def square_and_cube(num):
    square = num ** 2
    cube = num ** 3
    return square, cube
print(square_and_cube(3))

# Write a function that reverses a string.
def reverse_string(s):
    s = s[::-1]
    return s
print(reverse_string("Sonal"))

# 🔹 Level 2: Slightly Advanced Logic

# Check whether a number is a prime number or not using a function.
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1): # to check for prime number we need to check if the number is divisible by any number from 2 to the square root of the number.
        if num % i == 0: 
            return False # if the number is divisible by any number from 2 to the square root of the number then it is not a prime number. 
        return True # if it is not divisible by any number from 2 to the square root of the number then it is a prime number.
print(is_prime(7))

# Write a function to count vowels and consonants in a string.

def vowels_and_cons(s):
    vowels = "aeiouAEIOU"
    vowels_count = consonants_count = 0
    for char in s:
        if char.isalpha(): # Check if the character is an alphabet. isalpha() is a built-in function in python to check if the character is alphabet or not.
            if char in vowels:
                vowels_count += 1
            else: 
                consonants_count += 1
    return vowels_count, consonants_count
print(vowels_and_cons("Sonal"))

# Sum of Digits in a Mixed String.

def sum_of_digits(s):
    total = 0
    for char in s:
        if char.isdigit():        # Check if it's a digit (0-9)
            total += int(char)    # Convert to int and add to total
    return total

print(sum_of_digits("ahvc98jkgf5478nmmm43"))  # Output: 48

# Write a function to check if a string is a palindrome.

def is_palindrome(s):
    s = s.lower() # convert the string to lower case to ignore case sensitivity.
    return s == s[::-1] # check if the string is equal to it's reverse.
print(is_palindrome("racecar"))

# Write a function that returns the sum of digits of a number.

def sum_of_digits(n):
    total = 0
    for digit in str(n): # convert the number to string to iterate through each digit.
        total += int(digit) # convert the digit back to int and add it to total.
    return total
print(sum_of_digits(12345))

# Create a function that returns the nth Fibonacci number. 0, 1, 1, 2, 3, 5, 8, 13,.....etc.

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a
print(fibonacci(5))

# create a function to print fibonacci series.

def fibonacci_series(n):
    a, b = 0, 1
   
    for i in range(n):
        print(a, end=", ")
        a,b = b, a+b

fibonacci_series(6)


# Write a function that accepts a list and returns only even numbers.

def even_num_list(lst):
    even_number = []
    for num in lst:
        if num%2 == 0:
            even_number.append(num)
    return even_number
print("\n")
print(even_num_list([1,2,3,4,5,6,7,8,9,10]))


# Create a function that accepts a number and returns whether it is a perfect number or not.
# Perfect Number: A number that is equal to the sum of its proper divisors (excluding itself).
# Example:
# 6 → 1 + 2 + 3 = 6 → Perfect
# 28 → 1 + 2 + 4 + 7 + 14 = 28 → Perfect
# 12 → 1 + 2 + 3 + 4 + 6 = 16 → Not perfect
def is_perfect_number(n):
    sum_of_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i 
    return sum_of_divisors == n #  check if the sum of divisors is equal to the number.
print(is_perfect_number(6))

# 🔹 Level 3: Functions with Recursion and Nested Functions

# Write a recursive function to calculate factorial.
def factorial(n):
    if n==0 or n==1:
        return 1
    else: 
        return n * factorial(n-1)
print(factorial(5))

# Write a recursive function to calculate nth Fibonacci number.
# 0, 1, 1, 2, 3, 5, 8, 13,.....etc.
def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
print(fibonacci_recursive(5))

# Recursive Fibonacci Series Printer

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def print_fibonacci_series(terms):
    for i in range(terms):
        print(fibonacci(i), end=' ')

# Try it
print_fibonacci_series(10)

# Write a function that contains an inner function to check if a number is prime.
def check_number(num):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

# Try it
check_number(7)
check_number(10)



# Make a closure that counts down from a given number every time it’s called.
def countdown(n):
    def inner():
        nonlocal n # esliye define kiya coz edhr ye value change hoti rahegi n k which needs to be nonlocal.
        if n > 0:
            print(n)
            n -= 1
        else:
            print("countdown finished!")
    return inner
countdown_func = countdown(5)
countdown_func()
countdown_func()
countdown_func()
countdown_func()
countdown_func()
countdown_func()

# Create a function that returns another function to multiply by a given number (function factory).
def multiplier_factory(n):
    def multiply(x):
        return x * n
    return multiply

# Try it
times3 = multiplier_factory(3)
times5 = multiplier_factory(5)

print(times3(10))  # Output: 30
print(times5(4))   # Output: 20


# 🔹 Level 4: Functions with Default, Keyword, and Variable Arguments
# Write a function with default arguments.
# Example: def greet(name="Guest")
def greet(name="Guest"):
    print(f"Hello, {name}!")

# Try it
greet("Alice")  # Hello, Alice!
greet()         # Hello, Guest!


# Write a function that accepts any number of arguments and returns their sum.
# Use *args.

def total_sum(*args):
    return sum(args)

# Try it
print(total_sum(1, 2, 3))          # Output: 6
print(total_sum(5, 10, 15, 20))    # Output: 50
print(total_sum())                # Output: 0


# Write a function that accepts named arguments and prints them.
# Use **kwargs.

# **kwargs collects all keyword arguments into a dictionary.
# This is great when you don’t know in advance how many named parameters might be passed.
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Try it
print_info(name="Alice", age=25, city="Delhi")














# 🔹 Level 1: Basic Function Practice
# Write a function to add two numbers.

# python
# Copy
# Edit
# def add(a, b):
#     return a + b
# Write a function that returns whether a number is even or odd.

# Write a function that takes a name and prints a greeting.
# Example: "Hello, John!"

# Write a function to find the factorial of a number.

# Write a function to return the maximum of three numbers.

# Write a function that returns the square and cube of a number.

# Write a function that reverses a string.

# 🔹 Level 2: Slightly Advanced Logic
# Check whether a number is a prime number or not using a function.

# Write a function to count vowels and consonants in a string.

# Write a function to check if a string is a palindrome.

# Write a function that returns the sum of digits of a number.

# Create a function that returns the nth Fibonacci number.

# Write a function that accepts a list and returns only even numbers.

# Create a function that accepts a number and returns whether it is a perfect number or not.

# 🔹 Level 3: Functions with Recursion and Nested Functions
# Write a recursive function to calculate factorial.

# Write a recursive function to calculate nth Fibonacci number.

# Write a function that contains an inner function to check if a number is prime.

# Make a closure that counts down from a given number every time it’s called.

# Create a function that returns another function to multiply by a given number (function factory).

# 🔹 Level 4: Functions with Default, Keyword, and Variable Arguments
# Write a function with default arguments.
# Example: def greet(name="Guest")

# Write a function that accepts any number of arguments and returns their sum.
# Use *args.

# Write a function that accepts named arguments and prints them.
# Use **kwargs.

# 🔹 Bonus: Real-World Style Function Questions
# Write a function to validate an email address.

# Create a calculator using functions: add, subtract, multiply, divide.

# Create a shopping cart system using functions — add item, remove item, view cart.



