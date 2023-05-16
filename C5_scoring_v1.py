"""Component 5 - Scoring v1 - based on check_answer v3
Add +1 to score for every correct answer
"""
import random


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
    while question_number <= 10:
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

    print(f"\nThat is the end of the quiz! Your score is {score}/10! ")


# Main routine
establish_quiz()
