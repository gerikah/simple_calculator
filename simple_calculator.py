# Object Oriented Programming CMPE-103 PROGRAMMING EXERCISES : Assignment 5
# ALDAY, Gerikah L. - BSCPE 1-5


# ask the user to choose one of the four math operations
while True:
    # handle errors
    try:
        operation = input("Choose one mathematical operation (+, -, *, /): ")
        if operation not in ["+", "-", "*", "/"]:
            raise ValueError
        break
    except ValueError:
        print("Invalid operation. Please try again.")

# ask the user for two numbers
# handle errors

# perform calculations

# display result

# ask is the user wants to try again or not
    # handle errors
    # if yes:
        # repeat the first step
    # if no, end the program