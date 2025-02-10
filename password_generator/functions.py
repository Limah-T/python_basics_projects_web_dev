import random

alphabets = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
symbols = list("!#$%&()*+,-./:;<=>?@[]^_`{|}~")
numbers = list("0123456789")

def random_password(num_of_letter, num_of_num, num_of_sym):
    """Selects no of letters, numbers, and symbols based on user's input and randomly pick 
    from the lists(alphabets, numbers, symbols)"""

    password = (
        random.choices(alphabets, k=num_of_letter) +
        random.choices(numbers, k=num_of_num) +
        random.choices(symbols, k=num_of_sym)
    )

    random.shuffle(password)
    strong_password = "".join(password)
    print(f'✅ Here is your password: "{strong_password}"')
