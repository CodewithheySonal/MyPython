# modules is used to import all the modules(other python files) needed for the project.

import math
import random
import functions


print(math.pi)
# if we used from math import pi then we can directly use print(pie)
print(math.sqrt(16))

print(random.choice("123"))

functions.hello() # this will print Hello, World!. This will use this function from functions.py file.