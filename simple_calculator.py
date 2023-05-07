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
            operation = input("Choose one mathematical operation (+, -, *, /): ")
            if operation not in ["+", "-", "*", "/"]:
                raise ValueError
            break
        except ValueError:
            print("Invalid operation. Please try again.")

    # ask the user for two numbers
    while True:
        # handle errors
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

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
        print("Error: Cannot divide by zero.")
        # Set result to None if there is an error
        result = None  

    # display result if calculated
    if result is not None:
        print("The result of {} {} {} is {}".format(num1, operation, num2, result))

    # ask if the user wants to try again
    while True:
        # handle errors
        try:
            answer = input("Do you want to try again? (yes/no): ")
            if answer not in ["yes", "no"]:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter 'yes' or 'no'.")

    if answer == "no":
        print("Thank you for using this calculator.")
        break # exit the outer while loop if the user does not want to try again
