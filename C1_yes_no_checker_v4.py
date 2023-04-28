""" Component 1 - Yes/No checker v4 - based on v3
Turn code into a function
"""


def yes_no(question_text):

    while True:

        # Ask the user if they want instructions
        answer = input(question_text).lower()

        # If answer is yes, show instructions
        if answer == 'yes' or answer == 'y':
            answer = 'Yes'
            return answer

        # If answer is no, continue program
        elif answer == 'no' or answer == 'n':
            answer = 'No'
            return answer

        # Anything else, print error
        else:
            print("Please enter yes or no")


# Main routine
show_instruction = yes_no("Do you want to see the instructions?")
print(f"You entered {show_instruction}")
