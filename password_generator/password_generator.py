from functions import random_password

while True:
    try:
        letters = int(input("How many letters do you want? "))
        numbers = int(input("How many numbers do you want? "))
        symbols = int(input("How many symbols do you want? "))
        if any(x <= 0 for x in [letters, numbers, symbols]):
            print("⚠️ Each number must be greater than zero. Try again.")
            continue  # Restart loop
        
        total_num = letters + numbers + symbols
        if total_num < 8 or total_num > 12:
            print("⚠️ Total password length must be between 8 and 12. Try again.")
            continue  # Restart loop
        
        print(f"Generating a password with {letters} letters, {numbers} numbers, and {symbols} symbols......")
        random_password(letters, numbers, symbols)  
        break  # Exit loop after successful generation    

    except ValueError:
        print("⚠️ Only numbers are allowed!")
        