# closure is a function object that has access to variables in its Lexical scope(scope of it's parent)
# function after the parent function has finished executing.

# Let's create a closure game

# def parent_function(person):
#     coin = 4

#     def play_game(): # child function
#         nonlocal coin
#         coin -= 1

#         if coin > 1:
#             print(person + " has " + str(coin)+ " coins left")
#         elif coin == 1:
#             print(person + " has " + str(coin)+ " coin left")
#         else:
#             print(person + " has no coin left")

#     return play_game

# Sonal = parent_function("Sonal") # This will act as a closure variable which will store the function value for Sonal.
# Ruby = parent_function("Ruby")

# Sonal()
# Sonal()
# Ruby ()
# Sonal()
# Sonal()

# passing  coin as a parameter to the function.
def parent_function(person, coin):
    #coin = 4

    def play_game(): # child function
        nonlocal coin
        coin -= 1

        if coin > 1:
            print(person + " has " + str(coin)+ " coins left")
        elif coin == 1:
            print(person + " has " + str(coin)+ " coin left")
        else:
            print(person + " has no coin left")

    return play_game 

Sonal = parent_function("Sonal", 5) # This will act as a closure variable which will store the function value for Sonal.
Ruby = parent_function("Ruby", 3)

Sonal()
Sonal()
Ruby () 
Sonal()
Sonal()

