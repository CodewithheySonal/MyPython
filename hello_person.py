# command line arguments: these are the arguments passed to the script when it is run from the command line. //when you pass the argument in command line then only it will execute.

# https://docs.python.org/3/py-modindex.html

# import argparse # This is used to parse command line argument when you run the script from the command line. it is built in module in python. 

# parser = argparse.ArgumentParser( # this is used to create a parser object.
#     description = "Hello Person" 
# ) # this is used to create a description for the parser object. this will be displayed when you run the script with -h or --help option.
# parser.add_argument(
#     "--name",
#     required= True,
#     help= "Name of the person to greet"
# ) # this is used to add an argument to the parser object. this will be used to pass the name of the person to greet. this is a required argument. if you don't pass this argument then it will give an error.
# args = parser.parse_args() # this is used to parse the command line arguments. this will return an object with the arguments passed to the script.
# msg = f"Hello, {args.name}!"  
# print(msg)

# write this in command panel: py hello_person.py --name Sonal

# another example with functions and command line arguments.

def hello(name, lang):
    greetings = {
        "English": "Hello",
        "Spanish": "Hola",
        "German": "Hallo",
    }
    msg = f"{greetings[lang]} {name}!"
    print(msg)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personal greeting."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person to greet."
    )

    parser.add_argument(
        "-l", "--lang", metavar="language",
        required=True, choices=["English", "Spanish", "German"],
        help="The language of the greeting."
    )

    args = parser.parse_args()

    hello(args.name, args.lang)

# write this in command panel: py hello_person.py --name Sonal --l English


# Example coz according to me same we can do through functions()

# | 🔍 Feature                    | 🧩 **Function**                                             | 🖥️ **Command Line Argument**                                         |
# | ----------------------------- | ----------------------------------------------------------- | --------------------------------------------------------------------- |
# | 🎯 **Purpose**                | Code ko modular aur reusable banata hai                     | Program run hone ke waqt input provide karta hai                      |
# | 📥 **Input ka source**        | Function ke call ke time pe value dete hain (code ke andar) | Script run karte waqt terminal se input dete hain                     |
# | 🧠 **Use hota hai**           | Logic divide karne ke liye – jese `add()`, `greet()`, etc.  | Data ya parameters pass karne ke liye – jese `python script.py Alice` |
# | 🔁 **Reusability**            | Function ko baar-baar call kiya ja sakta hai                | CLI input ek baar run mein fix hoti hai                               |
# | 🔧 **Change karne ka tarika** | Code ke andar function call ko modify karo                  | Command line par argument badlo – code change nahi karna padta        |
# | 🤝 **User interaction**       | Nahi hoti (function sirf logic hai)                         | Indirect hoti hai, via command line                                   |
# | 📜 **Example**                | `greet("Alice")`                                            | `python greet.py Alice`                                               |
# | 🧰 **Use Cases**              | Calculator app, login logic, game functions                 | CLI tools, scripting, automation, quick test inputs                   |
