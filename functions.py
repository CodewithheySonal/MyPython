# functions to be used in the main.py file

# def hello():
#     print("Hello, World!")

# hello()

# def greet(name):
#     print(f"Hello, {name}!")

# greet("Sonal")  

# def add(a, b):
#     return a + b

# result = add(10, 5)
# print(result)  

# #or

# def mul(num1, num2):
#     print(num1*num2)

# mul(10,5)

# total = sum(1,2)
# print(total)

# def sum(num1, num2):
#     return num1 + num2

# total = sum(1,2)
# print(total)

# def sum(num1, num2):
#     if(type(num1) is not int or type(num2) is not int):
#         return 0
#     return num1 + num2

# total = sum("pyaaz",2)
# print(total)

# def multiple_items(*args): # *args is used to pass multiple arguments.
#     print(args)
#     print(type(args))

# multiple_items("Sonal", "Radha", "Manoj", "Sagar") 

def multiple_items_1(**kwargs): # *kwargs is used to pass multiple keyword arguments.
    print(kwargs)
    print(type(kwargs))

multiple_items_1(first="sonal", last="chouksey") 