""" Base component
All functions put in one code to see if they work together
"""
import random


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


def instructions_welcome(question_text):

    while True:

        # Ask the user if they want instructions
        answer = input(question_text).lower()

        # If answer is yes, show instructions
        if answer == 'yes' or answer == 'y':
            answer = 'Yes'
            print("Display instructions")
            return answer

        # If answer is no, continue program
        elif answer == 'no' or answer == 'n':
            answer = 'No'
            print("Continue program")
            return answer

        # Anything else, print error
        else:
            print("Please enter yes or no")


def establish_quiz():
    question_number = 1
    score = 0
    # List of Maori numbers and their corresponding English numbers
    number_mapping = {
        "Tahi": "One",
        "Rua": "Two",
        "Toru": "Three",
        "Wha": "Four",
        "Rima": "Five",
        "Ono": "Six",
        "Whitu": "Seven",
        "Waru": "Eight",
        "Iwa": "Nine",
        "Tekau": "Ten"
    }

    # Get a number from the list of Maori numbers
    numbers = list(number_mapping.keys())

    # Make sure that the rounds do not go over 10
    while question_number <= 10 and numbers:
        number = random.choice(numbers)
        answer = input(f"Question {question_number}\n"
                       f"What number is {number} in English? ")
        question_number += 1

        correct_answer = number_mapping[number]
        # Check answer
        if answer.capitalize() == correct_answer or answer == number \
                or answer == str(list(number_mapping.keys()).index(number) + 1):
            print(f"Correct! The answer was {correct_answer}.")
            # Component 5 - add score for correct answer
            score += 1
        else:
            print(f"That is wrong. The answer was {correct_answer}.")

        # Remove the chosen number from the list
        numbers.remove(number)

    print(f"\nThat is the end of the quiz! Your score is {score}/10!")


# main routine
user_details()  # Prompt for user details
welcome_response = instructions_welcome("Do you want instructions for the quiz? (Yes/No): ")

if welcome_response.lower() == 'yes':
    # Display instructions here
    print("These are the instructions for the quiz.")
    print("Please read them carefully.")

print("Starting the quiz...")
establish_quiz()
