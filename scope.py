# Scope is used to define a scope for the variables and functions in the program.
# The scope can be local, global, or built-in.
# Local scope: Variables defined inside a function are in the local scope of that function.
# Global scope: Variables defined outside of any function are in the global scope.
# Built-in scope: Variables and functions that are built into python are in the built-in scope.
# The scope of a variable is the region ogf the program where the variable is defined.

# name = "John" # Global scope

# def greetings():
#     age = 25 # Local scope
#     print(name)
#     print(age)


# greetings()

# name = "John"  # Global scope

# def greetings(name): # Local scope
#     age = 25  # Local scope
#     print(name)
#     print(age)

# greetings("Sonal") 

# def anotherfun():
#     greetings("Shonasss")

# anotherfun()

# def anotherfun():
#     age = 25 # Local Scope
#     def greetings(name): # Local scope
        
#         print(name)
#         print(age)

#     greetings("Sonal") 

# anotherfun()


name = "John"
count = 1

def fun():
    global count
    count += 1
    def innerfun():

     print(count)
     print(name)
    innerfun()

fun()

