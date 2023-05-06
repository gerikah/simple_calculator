# Object Oriented Programming CMPE-103 PROGRAMMING EXERCISES : Assignment 5
# ALDAY, Gerikah L. - BSCPE 1-5

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

    # display result
    print("The result of {} {} {} is {}".format(num1, operation, num2, result))

    # ask is the user wants to try again or not
    while True:
        # handle errors
        try:
            answer = input("Do you want to try again? (yes/no): ")
            if answer not in ["yes", "no"]:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter 'yes' or 'no'.")
    
    # if yes:
        # repeat the first step
    # if no, end the program