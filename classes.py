# classes in python are blueprints for creating objects.
# objects are instances of classes.

class Vehicle:
    def moves(self): # yaha self ko isliye kiya hai so that ye khudko refer kare
        # self is a reference to the current instance of the class.
        print("The Vehicle moves")

my_car = Vehicle() # my car is the object of vehicle class
my_car.moves() # ye esliye likha hai coz esko use krke function ko call karna hai

class Vehicle:
    def __init__(self, make, model): # this is the constructor method. It is called when an object is created from the class. 
        # __init__ : eska use hota hai to initialize the attributes of the class.
        self.make = make
        self.model = model
        pass
    def moves(self): 
        print("The Vehicle moves")

my_car = Vehicle('Toyota', 'corolla') 
print(f"My car is a {my_car.make} and model is {my_car.model}") 
my_car.moves()

# or

class Vehicle: # ye class ka name hai
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print('Moves along..')

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")


my_car = Vehicle('Tesla', 'Model 3') # ye object banaya hai vehicle class ka

# print(my_car.make)
# print(my_car.model)
my_car.get_make_model()
my_car.moves()

# Inheritance: It allows a class to inherit attributes and methods from another class.
# Inheritance is a way to form new classes using classes that have already been defined.


class Aircraft(Vehicle): # ye aircraft class hai jo inheritance perform kar raha hai vehicle class se
    def moves(self):
        print("The Aircraft flies")

class Truck(Vehicle):
    def moves(self):
        print("The Truck drives on the road")

class Bike(Vehicle):
    def moves(self):
        print("The Bike rides on the road")

my_plane = Aircraft("AirIndia", "AIR345")
my_truck = Truck("Tata", "T65")
my_bike = Bike("Java", "J800")

my_plane.get_make_model()
my_plane.moves()

my_truck.get_make_model()
my_truck.moves()

my_bike.get_make_model()
my_bike.moves()

# also we can use the __init_method of the parent class in the child class. Also, we can use super() to call the parent class's __init__ method.

class Aircraft(Vehicle):
    def __init__(self, make, model, id):
        # self.make = make
        # self.model = model
        super().__init__(make, model) # ye override karta hai parent class ke __init__ method ko
        self.id = id

    def moves(self):
        print(f"The Aircraft with {self.id} flies")

my_plane = Aircraft("AirIndia", "AIR345", "N627OJ")

my_plane.get_make_model()
my_plane.moves()

# Polymorphism: It allows methods to do different things based on the object it is acting upon, even if they share the same name.
# poly means many and morph means forms. So, polymorphism means many forms.
# In this case, the moves method is polymorphic because it behaves differently for different objects.
print('\n\n')

for v in (my_car, my_plane, my_truck, my_bike): # yahan ham polymorphism ka use kar rahe hain 
    v.get_make_model()
    v.moves()

print("\n\n\n")

# Some more examples to understand these concepts better.

# Simple:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old")

my_name = Person("Sonal", 24)
my_name.greet()


print("\n\n\n\n\n")



# Inheritance:
class Animal:
    def __init__(self, species):
        self.species = species
        pass # pass likhne ka matlab hai ki yahan koi code nahi hai, eska use syntax error se bachne k liye kiya jaata hai
    def make_sound(self):
        print(f"Generic animal sound")

class Dog(Animal):
    def __init__(self, species, sound, name):
        super().__init__(species)
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} the {self.species} barks: {self.sound}")

class Cat(Animal):
    def __init__(self, species, sound, name):
        super().__init__(species)
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} the {self.species} barks: {self.sound}")

my_dog = Dog("Dog", "Woof", "Jimmy")
my_cat = Cat("Cat", "Meow", "Kitty")

my_dog.make_sound()
my_cat.make_sound()

# polymorphism
print("\n\n")
# Using the Animal, Dog, Cat classes from above

def animal_action(Animal):
    Animal.make_sound()

generic_animal = Animal("Leo")
my_dog = Dog("Dog", "Woof","Labrador")
my_cat = Cat("Cat", "Meow", "Persian")

animal_action(generic_animal)
animal_action(my_dog)
animal_action(my_cat)

#4. Real-world Scenarios (Thoda Advance):

# Bank Account System:
# BankAccount class banayein (account_number, balance).
# Methods: deposit(), withdraw(), get_balance().
# SavingsAccount aur CheckingAccount classes banayein jo BankAccount se inherit karein.
# SavingsAccount mein interest_rate attribute add karein aur apply_interest() method.
# CheckingAccount mein overdraft_limit attribute add karein aur withdraw() method ko modify karein overdraft check karne ke liye.


# Shape Calculator:
# Shape abstract class (ya simply ek base class) banayein.
# Methods: area(), perimeter().
# Circle, Rectangle, Triangle classes banayein jo Shape se inherit karein.
# Har class mein area() aur perimeter() methods ko override karein.
# Polymorphism ka use karte hue, ek list mein alag-alag shapes ke objects rakhein aur loop karke har shape ka area aur perimeter calculate karein.


# Employee Management System:
# Employee class banayein (name, employee_id, salary).
# Methods: get_details(), calculate_annual_salary().
# Manager aur Developer classes banayein jo Employee se inherit karein.
# Manager mein department attribute, Developer mein programming_language attribute.
# Extra methods add karein jaisa tumhe theek lage.