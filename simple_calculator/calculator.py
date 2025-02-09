from functions import addition, subtraction, multiplication, division, firstnum, secondnum, operators, clear_screen

number1 = firstnum()
def cal_operation():
    """Perform user's mathematical operations based on user's numberic input values and allowed operations along with imported functions from functions modules."""
    global number1
    while True:
        print(operators())
        select_op = input("Enter operator: ")
        if select_op in operators():
            number2 = secondnum()
            if select_op == "+":
                result = addition(number1, number2)
            elif select_op == "-":
                result = subtraction(number1, number2)
            elif select_op == "*":
                result = multiplication(number1, number2)
            else:
                result = division(number1, number2)
            more_calulations = input(f"Enter 'x' to continue from {result}, 'y' to start over again, 'z' to quit: ").lower()
            if not continue_calculation(answer=result, more_cal_input=more_calulations):
                break
        else:
            print("Wrong operator selection!")

def continue_calculation(answer, more_cal_input):
    """Performs operations to continue, or start over, or quit based on user's string input(x, or y, or z)"""
    global number1
    if more_cal_input == 'x':
        number1 = answer
        return True
    elif more_cal_input == 'y':
        clear_screen()
        number1 = firstnum()
        return True
    else:
        print("Bye!")
        return False

# Calls the functions to execute program.    
cal_operation()
