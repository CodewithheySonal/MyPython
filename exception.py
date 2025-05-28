# Exceptions are events that can modify the flow of a program.
# They are used to handle errors or unexpected situations that occur during the execution of a program.
# In python, exceptions are raised when an error occurs, and they can be caught and handled using try-except blocks.
# This allows the program running to continue executing even if an error occurs, rather than crashing.

# print(x) this will raise NameError: name 'x' is not defined

# try:
#     print(x)
# except:
#     print("An error occurred.")

# try:
#     # print(x)
# except NameError:
#     print("NameError means that something is not defined.")

# print("\n\n")

x = 2
try:
    print(x / 0)
except NameError:
    print("NameError means that something is not defined.")
except ZeroDivisionError:
    print("ZeroDivisionError means that you cannot divide by zero.")

print("\n\n")

x = 2
try:
    print(x / 2)
except NameError:
    print("NameError means that something is not defined.")
except ZeroDivisionError:
    print("ZeroDivisionError means that you cannot divide by zero.")
else:
    print("No error Occurred!")
    
print("\n\n")

x = 2
try:
    print(x / 2)
except NameError:
    print("NameError means that something is not defined.")
except ZeroDivisionError:
    print("ZeroDivisionError means that you cannot divide by zero.")
else:
    print("No error Occurred!")
finally:
    print("I will print no matter what happens!")

x = 2
try:
    # print(x / 2)
    if not type(x) is str:
        raise TypeError("x is not a string")
except NameError:
    print("NameError means that something is not defined.")
except ZeroDivisionError:
    print("ZeroDivisionError means that you cannot divide by zero.")
except Exception as error:
    print(error)
else:
    print("No error Occurred!")
finally:
    print("I will print no matter what happens!")


class JustNotCoolError(Exception):
    pass
x = 2
try:
    raise JustNotCoolError("This just isn't cool, man.")
    # raise Exception("I'm a custom exception!")
except NameError:
    print("NameError means that something is not defined.")
except ZeroDivisionError:
    print("ZeroDivisionError means that you cannot divide by zero.")
except Exception as error:
    print(error)
else:
    print("No error Occurred!")
finally:
    print("I will print no matter what happens!")

