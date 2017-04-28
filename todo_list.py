"""This is a Terminal-based program that allows a user to create and edit a to-do list.

The stub of each function has been provided. Read the docstrings for what each 
function should do and complete the body of the functions below.

You can run the script in your Terminal at any time using the command:

    >>> python todo_list.py
SAMPLE COMMENT
"""

def add_to_list(my_list):
    """Takes user input and adds it as a new item to the end of the list."""

    print "The add_to_list function has not yet been written"


def view_list(my_list):
    """Print each item in the list."""

    print "The view_list function has not yet been written"


def display_main_menu(my_list):
    """Displays main options, takes in user input, and calls view or add function."""    
    

    while True:
        user_options = raw_input ("Would you like to: \nA. Add a new item \nB. View list \nC. Quit the program:\n")

        if user_options.upper() == "A":
            print "Add an animal to the zoo:"
            add_to_list("animal")
        elif user_options.upper() == "B" :
            print my_list
        else: 
            print "goodbye"
            break




#-------------------------------------------------

my_list = []
display_main_menu(my_list)

