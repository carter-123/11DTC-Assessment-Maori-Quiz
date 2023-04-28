""" Component 1 - Yes/No checker v2 - based on v1
Generate prompt which asks user if they want instructions
Add option to answer with 'y' or 'n'
"""

# Ask the user if they want instructions
show_instructions = input("Do you want to view the instructions? ")


# If they say yes, show instructions
if show_instructions == "yes" or show_instructions == "y":
    print("Display instructions")


# if they say no, continue program
elif show_instructions == "no" or show_instructions == "n":
    print("program continues")

# if they say anything else, ask the question again
else:
    print("Please enter yes or no")
