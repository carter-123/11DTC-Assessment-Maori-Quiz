""" Component 3 - Establish quiz v4 - based on v3
Change the numbers and answers into one list so they match with each other
"""
import random

question_number = 1

# Dictionary of Maori numbers and their corresponding English numbers
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

# Get a list of Maori numbers
numbers = list(number_mapping.keys())

while question_number <= 10:
    number = random.choice(numbers)
    answer = input(f"Question {question_number}\n"
                   f"What number is {number} in English? ")
    question_number += 1

    correct_answer = number_mapping[number]

    if answer.capitalize() == correct_answer:
        print(f"Correct! The answer was {correct_answer}.")
    else:
        print(f"That is wrong. The answer was {correct_answer}.")
