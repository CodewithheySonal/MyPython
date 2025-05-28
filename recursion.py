# recursion is used to solve problems that can be broken down into smaller subproblems.
# recursion is a function that calls itself to solve a problem.

# def add_one(num): 
#     if (num>=9):
#         return num + 1
#     total = num + 1
#     print(total) 

#     return add_one(total) # this is the recursive call to the function

# add_one(0) 

# def add_one(num): 
#     if (num>=9):
#         return num + 1
#     total = num + 1
#     print(total) 

#     add_one(total) # this is the recursive call to the function

# my_newtotal = add_one(0) 
# print(my_newtotal) # this will print the finsl value of the recursion.

def add_one(num): 
    if (num>=9):
        return num + 1
    total = num + 1
    print(total) 

    return add_one(total) # this is the recursive call to the function

my_newtotal = add_one(0) 
print(my_newtotal)

# Let's use this in rps game now 
# Below are the example i'm  trying for recursion.

#factorial of a number using recursion.

n = int(input("Enter a number to find the factorial: "))
def fac(n):
    if n == 0:
        return 1
    else:
        return n*fac(n-1)

print(f"The factorial of {n} is {fac(n)}")
