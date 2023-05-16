""" Component 1 - Get user details v2 - based on v1
Force user to enter an integer when inputting an age
"""

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
