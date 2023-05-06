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

# ask is the user wants to try again or not
    # handle errors
    # if yes:
        # repeat the first step
    # if no, end the program