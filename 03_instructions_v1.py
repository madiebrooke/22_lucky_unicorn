

# Function goes here
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower().strip()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or "n":
            response = "no"
            return response

        else:
            print("Please enter yes / no")


def instructions():
    print("**** How to play ****")
    print()
    print("The rules of the game go here")
    print()
    return ""


# Main Routine goes here...
show_instructions = yes_no("Have you played the game before? ")

if show_instructions == "no":
    instructions()

print("Program continues")
