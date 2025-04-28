#Loops in python
# A loop is a programming construct that repeats a group of statements.
# The most common types of loops are the for loop and the while loop.

# for loop is used to iterate over a sequence (like a list,tuple, dictionary, sets or string)
# The syntax for a for loop is:
# for variable in sequence:
# do something with variable

# while loop is used to excute a block of code as long as a condition is true.
# The syntax for a while loop is:
# while condition:
# do something

# value = 0
# while value <=10:
#     print(value)
#     value += 1


# value = 0
# while value <=10:
#     print(value)
#     if value == 5:
#       break # it will break the loop when value is 5.
#     value += 1

# value = 0
# while value <=10:
#     value += 1
#     if value == 5:
#      continue # it will skip the value 5 and continue to the next iteration.
#     print(value)
# else:
#     print("Loop is finished. Your current value is:", str(value))


# value = 2
# i = 1
# while i <=10:
#     value = value * i
#     print(f"{value}*{i} = {value}") # Formatted string literals(f-strings) are a way to format strings in Python.
#     # f-strings are prefixed with 'f' or 'F' are allow you to embed expressions inside string literals, using curly braces {}.
#     i += 1

# my_list = [1, 2, 3, 4]
# i = 0
# while i < len(my_list):
#     print(my_list[i])
#     i += 1


# for Loop:

# names = [ "Sonal", "Riya", "Sita"]
# for name in names:
#     print(name) # it will print all the names in the list.

# for i in "Sonalchouksey":
#     print(i) # it will print all the caharacters in the string.

# for x in names:
#     if x == "Riya":
#         break
#     print(x) # it will print all names until it reaches "Riya".

# for x in names:
#     if x == "Riya":
#         continue
#     print(x) # it will print all names except "Riya".

# for i in range(5): # range(stop) it will print number from 0 to stop-1.
#     print(i) # it will print numbers from 0 to 4.

# for i in range(2, 5): # range(start, stop, step) it will print numbers from start to stop-1 with step. 
#     print(i)

# for i in range(0, 50, 5): # the step is 5 which means it will print numbers from 0 to 50 with step of 5.
#     print(i)
# else:
#     print("I'm glad that's finished.")

# names = [ "Sonal", "Riya", "Sita"]
# actions = ["codes", "sings", "dances"]

# for name in names:
#     for action in actions:
#         print(name, "", action)

# for action in actions:
#     for name in names:
#         print(name, "", action)