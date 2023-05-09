""" Component 3 - Establish quiz v1
Generate a random maori number from a list
"""
import random
# List of maori numbers
numbers = ["Tahi", "Rua", "Toru", "Wha", "Rima", "Ono", "Whitu", "Waru", "Iwa", "Tekau"]

# Picking random number from the list
for item in range(20):
    number = random.choice(numbers)
    print(number)
