import random, os

def generate_random_number():
    """Print what number range for user to guess and generate a random number"""
    print("Guess a random number from 1 to 50")
    random_number = random.randint(1, 50)
    return random_number

def game_function(attempts):
    """Compare user numberic value to the random number generated, calculate user's attempts to guess right, tells user if number is too low or high."""
    random_number = generate_random_number()
    while True:
        try:
            guessed_number = int(input("Guess the number: "))
            if guessed_number == random_number:
                attempts -= 1
                print(f"Correct, you guessed right, with {3 - attempts} attempt(s) from 3")
                break
            elif guessed_number < random_number:
                attempts -= 1
                if random_number - guessed_number <= 5:
                    print("Number is too low, but you're very close")
                else:
                    print("Number is too low")
                print(f"You have {attempts} attempt(s) left!")
            elif guessed_number > random_number:
                attempts -= 1
                if guessed_number - random_number <= 5:
                    print("Number too high, but you're very close") 
                else:
                    print("Number is too high")
                print(f"You have {attempts} attempt(s) left!")
            if attempts == 0:
                print("Game Over!") 
                break
        except ValueError:
            print("Only numbers are allowed!")
              
attempts = 3
def continue_playing(play_again):
    """Allows user to play again based on the required string input 'yes' or 'no'"""
    global attempts
    if play_again == "yes" or play_again == "y":
        clear_screen()
        return True
    else:
        print("Bye!")
        return False
        
def clear_screen():
    """Clears user's screen to play again"""
    os.system('cls') if os.name == 'nt' else os.system('clear')