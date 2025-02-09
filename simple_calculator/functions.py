import os

def addition(num1, num2):
    """Adds two arguments passed to parameter num1 and num2"""
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
    return result

def subtraction(num1, num2):
    """Substracts two arguments passed to parameter num1 and num2"""
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
    return result

def multiplication(num1, num2):
    """Multiply two arguments passed to parameter num1 and num2"""
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
    return result

def division(num1, num2):
    """Divides two arguments passed to parameter num1 and num2 and
    and handle zero division error"""
    if num2 != 0:
        result =  num1 / num2
        print(f"{num1} / {num2} = {result}")
        return result
    else:
        print(f"{num1} cannot be divided by {num2}")
        return num1
    
def firstnum():
    """Checks input from user if it is a numeric value else raise and
      error and tell user"""
    while True:
        try:
            number1 = float(input("Enter first number: "))
            return number1
        except ValueError:
            print("Only numbers are allowed!")
               
def secondnum():
    """Checks input from user if it is a numeric value else raise and error and tell user"""
    while True:
        try:
            number2 = float(input("Enter second number: "))
            return number2
        except ValueError:
            print("Only numbers are allowed!")
        
def operators():
    """list of operators allowed"""
    operators = ["+", "-", "*", "/"]
    return operators

def clear_screen():
    """Clears the screen for performing new calculations"""
    os.system('cls') if os.name == 'nt' else os.system('clear')
