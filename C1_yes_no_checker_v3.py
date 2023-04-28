""" Component 1 - Yes/No checker v3 - based on v2
Loop code for better efficiency
Force answer to be lowercase to prevent error with capital letters
"""

# Ask the user if they want instructions
show_instructions = ""

while show_instructions != 'x':

    show_instructions = input("Do you want to view the instructions? ").lower()
    # If they say yes, show instructions
    if show_instructions == "yes" or show_instructions == "y":
        print("Display instructions")

    # if they say no, continue program
    elif show_instructions == "no" or show_instructions == "n":
        print("program continues")

    # if they say anything else, ask the question again
    else:
        print("Please enter yes or no")
