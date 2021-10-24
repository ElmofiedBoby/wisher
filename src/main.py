from storage import *
from process import process_inputs

def main():
    print("Welcome to Wisher!")

    logged_in = False
    current_user = None

    user_input = input("> ")
    if user_input != "quit" and user_input != "exit":
        logged_in, current_user = process_inputs(user_input, logged_in, current_user)
    else:
        print("Quitting...")

    while user_input != "quit" and user_input != "exit":
        user_input = input("> ")
        logged_in, current_user = process_inputs(user_input,  logged_in, current_user)

if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main() 