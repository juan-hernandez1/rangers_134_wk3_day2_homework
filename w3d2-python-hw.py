# Exercise 1 - Turn the shopping cart program from last week into an object-oriented program
# The comments in the cell below are there as a guide for thinking about the problem. However, if you feel a different way is best for you and your own thought process, please do what feels best for you by all means.

# Create a class called cart that retains items and has methods to add, remove, and show

class Cart():
  
    def __init__(self):
        self.cart = {}

    def add_item(self, item, quantity):
        self.cart[item] = self.cart.get(item, 0) + quantity

    def takeout(self, item, quantity):
        if item in self.cart and self.cart[item] >= quantity:
            self.cart[item] -= quantity

    def view_cart(self):
        print("This is what is in your cart:")
        for item, quantity in self.cart.items():
            print(f"{item}: {quantity}")
            

cart = Cart()

while True:

    response = input("What would you like to do? add/remove/view/quit: ")

    if response == "add":
        new_item = input("What would you like to add? ")        
        quantity = int(input(f"How many {new_item} would you like to add? "))
        cart.add_item(new_item, quantity)
        print(f"Qty {quantity}: {new_item}  has been added to your cart. ")
    elif response == "remove":
        takeout = input("What would you like to remove? ")
        quantity = int(input(f"How many {takeout} would you like to remove? "))
        cart.takeout(takeout, quantity)
        print(f"Qty {quantity}: {takeout} has been removed from your cart.")
    elif response == "view":           
            cart.view_cart()
    elif response == "quit":
        break
    else:
        print("Invalid input. Please choose add, remove, view, or quit.")

cart.view_cart()


# Exercise 2 - Write a Python class which has two methods get_String and print_String.
# get_String accept a string from the user and print_String print the string in upper case

class String1():
    def __init__(self):
        self.input_string = ""

    def get_String(self):
        self.input_string = input("Enter a string: ")

    def print_String(self):
        print(self.input_string.upper())

string_instance = String1()

string_instance.get_String()

string_instance.print_String()

    