""" Component 4 - Check user answer v1 - based on establish_quiz v2
Put in correct answer for each maori number
"""
import random

question_number = 1

# List of Maori numbers
numbers = ["Tahi", "Rua", "Toru", "Wha", "Rima", "Ono", "Whitu", "Waru", "Iwa", "Tekau"]

answers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

while question_number <= 10:
    number = random.choice(numbers)
    answer = input(f"Question {question_number}\n"
                   f"What number is {number} in English? ")
    question_number += 1

