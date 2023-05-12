""" Component 1 - Instructions checker v4 - based on v3
Turn code into a function
"""


def instructions_welcome(question_text):

    while True:

        # Ask the user if they want instructions
        answer = input(question_text).lower()

        # If answer is yes, show instructions
        if answer == 'yes' or answer == 'y':
            answer = 'Yes'
            print("Display instructions")
            return answer

        # If answer is no, continue program
        elif answer == 'no' or answer == 'n':
            answer = 'No'
            print("Continue program")
            return answer

        # Anything else, print error
        else:
            print("Please enter yes or no")


# Main routine
show_instruction = instructions_welcome("Welcome to the Maori Quiz! "
                                        "\nDo you want to see the instructions? ")
print(f"You entered {show_instruction}")
