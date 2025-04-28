

# All Datatypes in python 

First = 'Sonal'
Last = 'Chouksey'

print(First + " " + Last) #string concatenation
print(type(First))
print(type(Last) == str) #string comparison
print(type(Last) is str) #string comparison

decade = str(2020) #string conversion or casting. Here str is a constructor function.
print(decade + "s")

# Multiline print statement

multiline = ''' This is a multiline statement.
            do you understand it?
            I hope you do. '''
print(multiline)

# Handling special characters in string
print("my name is \"Sonal\" Chouksey. I\'m a data engineer\t what about you?\n are you also a DE?") 

# String Methods

Meth = "Hey how are you?"

print(Meth.upper()) #convert to upper case
print(Meth.title()) #convert first letter of each word to upper case
print(len(Meth)) #Lenght of string
print(Meth.replace("Hey", "Hello")) #replace a word in string
print(Meth.split()) #split the string into list of words

#Build a Menu

show = "menu".upper()
print(show.center(20,"=")) #center the string in 20 spaces with "=" as padding
print("1. Pizza".ljust(18,"-")+ "10$".rjust(2,"-")) #shift+alt+down arrow to copy paste this line
print("2. Momos".ljust(18,"-")+ "5$".rjust(2,"-"))
print("3. Samosa".ljust(18,"-")+ "2$".rjust(2,"-"))
print("4. Sandwich".ljust(18,"-")+ "10$".rjust(2,"-"))
print("5. Pasta".ljust(18,"-")+ "10$".rjust(2,"-"))
print("")

# String Index values

print(Meth[0])
print(Meth[1])
print(Meth[-1])
print(Meth[1:-1])

# Some Bollean data

print(Meth.startswith("H"))
print(Meth.endswith("H"))

# Numeric Datatypes

x = 100.804
y = int(700)
print(type(x))
print(isinstance(y, int)) #check if y is the instance of int class

# Built In Function

print(abs(x)) #absolute value of x
print(round(x)) #round off x to nearest integer
print(round(x,2)) #round off x to 2 decimal places

# import Math module

import math
print(math.pi)
print(math.floor(x))
print(math.ceil(x))

# casting a string to a number

my_value = "3456"
my_cvalue = int(my_value)
print(type(my_value))
print(type(my_cvalue))