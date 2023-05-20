""" Component 3 - Establish quiz v4 - based on v3
Allow the answer to be both the written word answer or the integer answer
Turn it into a function
"""
import random


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
    while question_number <= 10 and numbers:
        number = random.choice(numbers)
        answer = input(f"Question {question_number}\n"
                       f"What number is {number} in English? ")
        question_number += 1

        correct_answer = number_list[number]
        # Check answer
        if answer.capitalize() == correct_answer or answer == number \
                or answer == str(list(number_list.keys()).index(number) + 1):
            # Component 5 - add score for correct answer
            score += 1
            print(f"Correct! The answer was {correct_answer}. Your score is {score}!")
        else:
            print(f"That is wrong. The answer was {correct_answer}. Your score is {score}.")

        # Remove the chosen number from the list
        numbers.remove(number)

    print(f"\nThat is the end of the quiz! Your score is {score}/10!")


establish_quiz()
