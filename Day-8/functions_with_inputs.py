# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.


def greet():
    print("hello")
    print("How do you do?")
    print("Isn't the weather nice today?")

greet()


# 2 parameters and calling with 2 arguments

def greet_eith_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}")

greet_eith_name("john")

# functions with positional arguments

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"Your location {location}")
    
greet_with(name="john", location="no where")