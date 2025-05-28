# Lambda is a small anonymous function. It can take any number of arguments, but can only have one expression.
# It is a function that is defined without a name. It can be used when you need a nameless function for a short period of time.
# It is often used as an argument to higher-order functions (functions that take other functions as arguments).
# Syntax: Lambda arguments: expression


squared = lambda num : num * num
print(squared(5))

addtwo = lambda num: num + 2
print(addtwo(5))

sum = lambda a, b: a + b
print(sum(5,5))

# Lambda functions can be used with filter(), map(), and reduce() functions.

def funcbuilder(x): # x is a parameter
    return lambda num: num + x # num is a parameter of the lambda function which is an argument to the function returned by funcbuilder.

addfive = funcbuilder(5) # this will return a lambda function that takes one argument and adds 5 to it.
addnine = funcbuilder(9)

print(addfive(10)) # this will pass 10 to the lambda function
print(addnine(10))

# map() function is used to apply a function to all the items in an iterable (List, Tuple, etc.) and return a map object (which is an iterator).
# The map object can be converted to a list or tuple using the list() or tuple() functions.
# The function is applied to each item in the iterable and the result is returned as a map object.
# Syntax: map(function, iterable)
# Example: Square all numbers in a list

# 🔄 map() kab use karein?
# Aapko har item par koi operation lagani ho.
# List ke sab elements ko transform karna ho.

numbers = [2,4,5,7,14,11]
squared = map(lambda num: num * num, numbers)
print(list(squared))

# filter() function is used to filter items in an iterable (List, Tuple, etc.) based on a function that returns true or false.
# The filter object can be converted to a list or tuple using the list() or tuple() functions.
# Example: Filter all odd numbers in a list
# The function is applied to each item in the iterable and the items that return true are returned as a filter object.
# Syntax: filter(function, iterable)

# 🔍 filter() kab use karein?
# Aapko kuch items ko choose karna ho list se based on condition.

odd_numbers = filter(lambda num: num % 2 != 0, numbers)
print(list(odd_numbers))

# reduce() function is used to apply a function to all the items in an iterable (List, Tuple, etc.) and return a single value.
# The reduce object can be converted to a list or tuple using the list() or Tuple() functions.
# The function is applied to the first two items in the iterable and the result is passed to the function along with the next item in the iterable.
# This process is repeated until all items in the iterable have been processed.
#syntax: reduce(function, iterable, initializer)

# 🧮 reduce() kab use karein?
# Aapko poori list ko ek value mein convert karna ho.
# Accumulate karna ho (e.g., sum, product, maximum, etc.).

from functools import reduce
# Example: Sum of all numbers in a list
# sum_of_number = reduce(lambda acc, cum: acc + cum, numbers)
sum_of_number = reduce(lambda acc, cum: acc + cum, numbers, 10)
print(sum_of_number)

# example 2: count the number of characters in the string

names = ["Sonal Chouksey", "You are a good person", "I'm alive but dead from inside", "Still I manage to smile"]
count_characters = reduce(lambda acc, cum: acc + len(cum), names, 0) # agar initializer nahi diya to acc ki value first element ki length hogi
# acc= 0, cum ="Sonal Chouksey" => acc = 0+14 = 14
print(count_characters)


# 🧠 When to use sorted()?
# You want to sort data.
# You don’t want to modify the original list.
# You want custom sorting with key=.

# using sorted() function with lambda
pairs = [(1, 2), (3, 1), (5, 0)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  # Output: [(5, 0), (3, 1), (1, 2)]


# 🧠 1. Lambda Function kab use karein?

# Aapko ek chhoti anonymous function chahiye ho (without def).
# Function sirf ek hi expression ka ho.
# Ek hi baar use karna ho (temporary).