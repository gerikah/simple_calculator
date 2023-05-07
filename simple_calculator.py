# Object Oriented Programming CMPE-103 PROGRAMMING EXERCISES : Assignment 5
# ALDAY, Gerikah L. - BSCPE 1-5

import pyfiglet
border = "*" * 180
title = ("\n\n" + border + "\n\n" + "\033[95m" + pyfiglet.figlet_format("Calculator", justify = "center", font = "isometric1", width = 175) + "\n")
print(title)

while True:
    # ask the user to choose one of the four math operations
    while True:
        # handle errors
        try:
            print("\n\n" + border + "\n\n" + "\033[95m" + pyfiglet.figlet_format("Choose one mathemtical operation" , justify = "center", font = "cybermedium", width = 175) + '\n')
            print ("\n\033[95m" + pyfiglet.figlet_format(" +   -   *   / ", justify = "center", width = 175) + "\n" + border)
            operation = input(" ".center(85))
            if operation not in ["+", "-", "*", "/"]:
                raise ValueError
            break
        except ValueError:
            print("\n\n" + "\n\n" + "\033[95m" + pyfiglet.figlet_format("Invalid operation. Please try again.", justify = "center", font = "cybermedium", width = 175) + border)
    print ("\n\n" + "\033[95m" + pyfiglet.figlet_format(" operation selected", justify = "center", font = "cybermedium", width = 175))

    # ask the user for two numbers
    while True:
        # handle errors
        try:
            print("\n\n" + border + "\n\n" + "\033[95m" + pyfiglet.figlet_format("Enter the first number" , justify = "center", font = "cybermedium", width = 175))
            num1 = float(input(" ".center(85)))
            print("\n\n" + border + "\n\n" + "\033[95m" + pyfiglet.figlet_format("Enter the second number" , justify = "center", font = "cybermedium", width = 175))
            num2 = float(input(" ".center(85)))
            break
        except ValueError:
            print("\n\n" + "\n\n" + "\033[95m" + pyfiglet.figlet_format("Invalid input. Please try again.", justify = "center", font = "cybermedium", width = 175) + border)    
    
    # perform calculations
    # handle errors 
    try:
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        else:
            result = num1 / num2
    except ZeroDivisionError:
        print("\n\n" + border + "\n\n" + "\033[95m" + pyfiglet.figlet_format("Error. You cannot divide by zero", justify = "center", font = "cybermedium", width = 175))    
        # Set result to None if there is an error
        result = None

    # display result if calculated
    if result is not None:
        print("\n\n" + "\n\n" + "\033[95m" + pyfiglet.figlet_format("The  result  of  {}  {}  {}  is  {}".format(num1, operation, num2, result), justify = "center", width = 175) + border)

    # ask if the user wants to try again
    while True:
        # handle errors
        try:
            print(print("\n\n" + border + "\n\n" + "\033[95m" + pyfiglet.figlet_format("Do you want to try again? (yes/no)", justify = "center", font = "cybermedium", width = 175)))
            answer = input(" ".center(85))
            answer = answer.lower()
            if answer not in ["yes", "no"]:
                raise ValueError
            break
        except ValueError:
            print("\n\n" + "\n\n" + "\033[95m" + pyfiglet.figlet_format("Invalid input. Please enter 'yes' or 'no'", justify = "center", font = "cybermedium", width = 175) + border)    
    
    if answer == "no":
        print("\n\n" + border + "\n\n" + "\033[95m" + pyfiglet.figlet_format("Thank you for using this calculator.", justify = "center", width = 175))
        break # exit the outer while loop if the user does not want to try again
