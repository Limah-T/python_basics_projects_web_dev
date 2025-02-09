from functions import game_function, continue_playing, attempts

def main():
    """Executes the game program with the the imported functions from functions.py module"""
    global attempts
    game_function(attempts)
    while True:
        play_again = input("Enter 'yes' to play again, 'no' to exit: ").lower()
        if continue_playing(play_again):
            attempts = 3
            game_function(attempts)
        else:
            break 

if __name__ == "__main__":
    main()