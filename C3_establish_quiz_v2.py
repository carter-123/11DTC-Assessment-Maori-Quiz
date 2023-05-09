""" Component 3 - Establish quiz v2 - based on v1
Put in rounds and a round counter
"""
import random
rounds = 0
# List of maori numbers
numbers = ["Tahi", "Rua", "Toru", "Wha", "Rima", "Ono", "Whitu", "Waru", "Iwa", "Tekau"]


while rounds < 10:
    # Picking random number from the list
    for item in range(1):
        number = random.choice(numbers)
        input(f"What number is {number} in english? ")
        rounds += 1
