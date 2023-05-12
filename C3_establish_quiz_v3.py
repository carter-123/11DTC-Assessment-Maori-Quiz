""" Component 3 - Establish quiz v3 - based on v2
Put in correct answer for each maori number
"""
import random
question_number = 1
# List of maori numbers
numbers = ["Tahi", "Rua", "Toru", "Wha", "Rima", "Ono", "Whitu", "Waru", "Iwa", "Tekau"]


while question_number <= 10:
    # Picking random number from the list
    for item in range(1):
        number = random.choice(numbers)
        answer = input(f"Question {question_number}\n"
                       f"What number is {number} in english? ")
        question_number += 1
        if answer == number_answer:
            print(f"Correct! The answer was {number_answer}")
        else:
            print(f"That is wrong. The answer was {number_answer}")
