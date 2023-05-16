""" Component 1 - Get user details v3 - based on v2
Turn code into a function
"""


def user_details():
    user_name = input("What is your name? ")
    error = "Please enter a valid integer."
    valid = False

    while not valid:
        try:
            user_age = int(input("How old are you? "))

            print(f"Your name is {user_name} and you are {user_age} years old!")
            valid = True

        except ValueError:
            print(error)
