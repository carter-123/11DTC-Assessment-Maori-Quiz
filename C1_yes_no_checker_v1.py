""" Component 1 - Yes/No checker v1
Generate prompt which asks user if they want instructions
Ask again if answer is not yes or no
"""

# Ask the user if they want instructions
show_instructions = input("Do you want to view the instructions? ")


# If they say yes, show instructions
if show_instructions == "yes":
    print("Display instructions")


# if they say no, continue program
elif show_instructions == "no":
    print("program continues")

# if they say anything else, ask the question again
else:
    print("Please enter yes or no")
