""" Component 2 - Instructions v4 - based on v3
Turn code into a function
"""


def instructions_welcome(question_text):

    while True:

        # Ask the user if they want instructions
        answer = input(question_text).lower()

        # If answer is yes, show instructions
        if answer == 'yes' or answer == 'y':
            answer = 'Yes'
            print("Here are the instructions!")
            print()
            print("When you start, a question will give you a random number in Maori from 1-10")
            print()
            print("You must enter the correct english number to earn 1 point (can enter either the word or the number)")
            print()
            print("If you get it wrong, you don't get anything!")
            print()
            print("Good luck and have fun!")
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
