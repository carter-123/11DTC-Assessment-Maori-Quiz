""" Base component v1
All functions put in one code to see if they work together
"""
import random


# Function to get the user's details
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


# Function for instructions
def instructions_welcome(question_text):

    while True:

        # Ask the user if they want instructions
        answer = input(question_text).lower()

        # If answer is yes, show instructions
        if answer == 'yes' or answer == 'y':
            answer = 'Yes'
            print(formatter("=", "Here are the instructions!"))
            print()
            print("When you start, a question will give you a random number in Maori from 1-10")
            print()
            print("You must enter the correct english number to earn 1 point (can enter either the word or the number)")
            print()
            print("If you get it wrong, you don't get anything!")
            print()
            print("Good luck and have fun!")
            return answer

        # If answer is no, continue program
        elif answer == 'no' or answer == 'n':
            answer = 'No'
            print("Good luck and have fun!")
            return answer

        # Anything else, print error
        else:
            print("Please enter yes or no")


# Function for the quiz
def establish_quiz():
    question_number = 1
    score = 0
    # List of Maori numbers and their corresponding English numbers
    number_list = {
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
    numbers = list(number_list.keys())

    # Make sure that the rounds do not go over 10
    while question_number <= 10:
        number = random.choice(numbers)
        print(formatter(".", f"Question {question_number}"))
        print(formatter("?", f"What number is {number} in English?"))
        print()
        answer = input()
        question_number += 1

        correct_answer = number_list[number]
        # Check answer
        if answer.capitalize() == correct_answer or answer == number \
                or answer == str(list(number_list.keys()).index(number) + 1):
            print(formatter("!", f"Correct! The answer was {correct_answer}."))
            # Component 5 - add score for correct answer
            score += 1
        else:
            print(f"Nice try, but the answer was {correct_answer}.")

        # Remove the chosen number from the list
        numbers.remove(number)

    print(f"That is the end of the quiz! Your score is {score}/10! Great work!")


# Function for the formatter
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# main routine
print(formatter("*", "Welcome to the Maori quiz!"))
print()
welcome_response = instructions_welcome("Do you want instructions for the quiz? (Yes/No): ")
print("=" * 30)
# Prompt to pull function
user_details()

print("Starting the quiz...")
establish_quiz()
print(formatter("-", f"Thanks for playing! Goodbye!"))
